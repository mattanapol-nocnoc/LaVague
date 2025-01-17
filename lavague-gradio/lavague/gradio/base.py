from io import BytesIO
import queue
from typing import List, Optional
from lavague.core.agents import WebAgent
import gradio as gr
from PIL import Image

image_queue = queue.Queue()


class GradioAgentDemo:
    """
    Launch an agent gradio demo of lavague

    Args:
        driver (`BaseDriver`):
            The driver
        context (`ActionContext`):
            An action context
    """

    html = """
    <div class="list-container">
        <ul>
        </ul>
    </div>
    """

    css = """
        .my-button {
            max-height: 3rem !important;
            max-width: 5rem !important;
            min-width: min(100px,100%) !important;
    }
    """

    title = """
    <div class='parent' align="center">
    <div class='child' style="display: inline-block !important;">
    <img src="https://raw.githubusercontent.com/lavague-ai/LaVague/new_gradio/docs/assets/logo.png" width=40px/>
    </div>
    <div class='child' style="display: inline-block !important;">
    <h1>LaVague</h1>
    </div>
    </div>
    """

    title_history = """
    <div align="center">
    <h3>Steps</h3>
    </div>
    """

    def __init__(
        self,
        objective: str,
        instructions: Optional[List[str]],
        agent: WebAgent,
        user_data=None,
    ):
        self.objective = objective
        self.instructions = instructions
        self.agent = agent
        self.user_data = user_data
        self.previous_val = None

    def _init_driver(self):
        def init_driver_impl(url):
            self.agent.action_engine.driver.get(url)
            ret = self.agent.action_engine.driver.get_screenshot_as_png()
            ret = BytesIO(ret)
            ret = Image.open(ret)
            self.previous_val = ret
            image_queue.put(ret)
            return url

        return init_driver_impl

    def _process_instructions(self):
        def add_instruction(instruction, instructions_history):
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(instructions_history, "html.parser")
            new_item = soup.new_tag("li")
            new_item.string = instruction
            soup.find("ul").append(new_item)

            items = soup.find_all("li")
            for item in items:
                item.attrs.pop("style", None)

            items[-1]["style"] = "background-color: #555;"

            output = soup.prettify()
            return output

        def process_instructions_impl(
            objective, url_input, instructions_history, history
        ):
            history[-1][1] = "⏳ Thinking of next steps..."
            yield objective, url_input, instructions_history, history
            self.agent.action_engine.set_gradio_mode_all(True, None)
            self.agent.clean_screenshot_folder = False
            yield from self.agent._run_demo(
                objective,
                self.user_data,
                False,
                objective,
                url_input,
                instructions_history,
                history,
            )
            return objective, url_input, instructions_history, history

        return process_instructions_impl

    def __add_message(self):
        def clear_instructions(instruction, instructions_history):
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(instructions_history, "html.parser")
            soup.find("ul").clear()

            output = soup.prettify()
            return output

        def add_message(history, message, instructions_history):
            instructions_history = clear_instructions("", instructions_history)
            history.clear()
            history.append((None, None))
            return history, instructions_history

        return add_message

    def refresh_img_dislay(self, image_display):
        image = image_display
        try:
            image = image_queue.get(False)
        except:
            pass
        if image is not None:
            self.previous_val = image
        else:
            image = self.previous_val
        return image

    def launch(self, server_port=7860, share=True, debug=True):
        def toggle_to_url():
            return (
                gr.update(visible=True),
                gr.update(visible=False),
                gr.update(elem_classes=["selected", "my-button"]),
                gr.update(elem_classes=["unselected", "my-button"]),
            )

        def toggle_to_objective():
            return (
                gr.update(visible=False),
                gr.update(visible=True),
                gr.update(elem_classes=["unselected", "my-button"]),
                gr.update(elem_classes=["selected", "my-button"]),
            )

        with gr.Blocks(
            gr.themes.Default(primary_hue="blue", secondary_hue="neutral"), css=self.css
        ) as demo:
            with gr.Tab(""):
                with gr.Row():
                    gr.HTML(self.title)

                with gr.Row(equal_height=False):
                    with gr.Column():
                        with gr.Row():
                            with gr.Tabs(
                                selected=1
                                if self.agent.action_engine.driver.get_url() is not None
                                else 0
                            ) as tabs:
                                with gr.Tab("URL", id=0):
                                    url_input = gr.Textbox(
                                        value=self.agent.action_engine.driver.get_url(),
                                        scale=9,
                                        type="text",
                                        label="Enter URL and press 'Enter' to load the page.",
                                        visible=True,
                                    )
                                with gr.Tab("Objective", id=1) as tab:
                                    objective_input = gr.Textbox(
                                        value=self.objective,
                                        scale=9,
                                        type="text",
                                        label="Enter the objective and press 'Enter' to start processing it.",
                                        visible=True,
                                    )
                with gr.Row(variant="panel", equal_height=True):
                    with gr.Column(scale=7):
                        image_display = gr.Image(
                            label="Browser", interactive=False, height="70%"
                        )
                    with gr.Column(scale=3):
                        chatbot = gr.Chatbot(
                            [],
                            label="Agent output",
                            elem_id="history",
                            bubble_full_width=False,
                            height="70%",
                            placeholder="Agent output will be shown here\n",
                            layout="bubble",
                        )
                        instructions_history = gr.HTML(
                            "<div class='list-container'><ul></ul></div>"
                        )
                # objective submission handling
                objective_input.submit(
                    self.__add_message(),
                    inputs=[chatbot, objective_input, instructions_history],
                    outputs=[chatbot, instructions_history],
                ).then(
                    self._process_instructions(),
                    inputs=[objective_input, url_input, instructions_history, chatbot],
                    outputs=[objective_input, url_input, instructions_history, chatbot],
                )
                demo.load(
                    fn=self.refresh_img_dislay,
                    inputs=image_display,
                    outputs=image_display,
                    show_progress=False,
                    every=1,
                )
                # Use the image_updater generator function
                # submission handling
                url_input.submit(
                    self._init_driver(), inputs=[url_input], outputs=url_input
                )
                if self.agent.action_engine.driver.get_url() is not None:
                    ret = self.agent.action_engine.driver.get_screenshot_as_png()
                    ret = BytesIO(ret)
                    ret = Image.open(ret)
                    self.previous_val = ret
                    image_queue.put(ret)
        demo.launch(server_port=server_port, share=True, debug=True)
