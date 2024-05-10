---
description: "The open-source community for Large Action Models"
---

## 🏄‍♀️  What is LaVague?

LaVague is an **open-source Large Action Model framework** for turning **natural language** into **browser actions**.

At LaVague's core, we have an **Action Engine** which uses **advanced AI techniques** (RAG, Few-shot learning, Chain of Thought) to “compile” natural language instructions into browser automation code, by leveraging **Playwright** or **Selenium**.

## 🚀 Getting Started

### LaVague CLI

To test out LaVague with our Gradio demo interface you can download our CLI package and run the `lavague launch` command.

```bash
pip install lavague-cli
lavague launch
```

This will launch an interactive web interface where you can input a website URL and instructions to automate web actions.

For more information on the LaVague CLI package, see our [CLI guide](https://docs.lavague.ai/en/latest/docs/get-started/CLI)

### LaVague core

You can download LaVague our PyPi package with:

```bash
pip install lavague
```
You can then leverage our lavague-core library to generate and execute the code needed to perform web actions.

```python
from lavague.integrations.drivers.playright import PlayrightDriver
from lavague.integrations.contexts.apis.openai_api import OpenaiContext
from lavague import ActionEngine

URL = "https://news.ycombinator.com"
driver = PlayrightDriver(URL)
config = OpenaiContext.from_defaults()
action_engine = ActionEngine.from_context(driver, config)
action = action_engine.get_action("Enter LaVague inside the search bar and then press enter")
print(action)
```
For more informatio on this example and how to use LaVague Core, see our [quick-tour](https://docs.lavague.ai/en/latest/docs/get-started/quick-tour/).

!!! import "OPENAI_API_KEY"
    Note, these examples use our default OpenAI API configuration. You will need to set the OPENAI_API_KEY variable in your local environment with a valid API key for these to work. 
    
    For different API integrations, see our [integrations guide](https://docs.lavague.ai/en/latest/docs/integrations/home/).


## 🙋 Contributing

We would love your help and support on our quest to build a robust and reliable Large Action Model for web automation.

To avoid having multiple people working on the same things & being unable to merge your work, we have outlined the following contribution process:

1) 📢 We outline tasks on our [`backlog`](https://github.com/orgs/lavague-ai/projects/1/views/3): we recommend you check out issues with the [`help-wanted`](https://github.com/lavague-ai/LaVague/labels/help%20wanted) labels & [`good first issue`](https://github.com/lavague-ai/LaVague/labels/good%20first%20issue) labels

2) 🙋‍♀️ If you are interested in working on one of these tasks, comment on the issue!

3) 🤝 We will discuss with you and assign you the task with a [`community assigned`](https://github.com/lavague-ai/LaVague/labels/community-assigned) label

4) 💬 We will then be available to discuss this task with you

5) ⬆️ You should submit your work as a PR

6) ✅ We will review & merge your code or request changes/give feedback

Please check out our [`contributing guide`](docs/contributing/contributing.md) for a more detailed guide.

If you want to ask questions, contribute, or have proposals, please come on our [`Discord`](https://discord.gg/SDxn9KpqX9) to chat!

## 🗺️ Roadmap

TO keep up to date with our project backlog [here](https://github.com/orgs/lavague-ai/projects/1/views/2).

!!! warning "Disclaimer"

    This project executes LLM-generated code using `exec`. This is not considered a safe practice. We therefore recommend taking extra care when using LaVague (such as running LaVague in a sandboxed environment)!