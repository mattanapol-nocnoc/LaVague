# LaVague CLI

The Lavague CLI provides a fast way to get started with our `demo` and `eval` tools:

-  `demo` launches an interactive Gradio demo where you can perform web actions from natural language instructions
- `eval` allows you to evaluate the performance of the Large Action Model

!!! note "API key"
    - Our CLI uses the OpenAI API by default. You will need to have the OPENAI_API_KEY environment variable set  with a valid API key in your local environment.
    To use LaVague with different APIs, see our [integrations section](https://docs.lavague.ai/en/latest/docs/integrations/home/)

## LaVague demo
<div>
    <img src="https://raw.githubusercontent.com/lavague-ai/lavague/main/docs/assets/lavague_launch_hn.gif" alt="LaVague Launch Example">
</div>
You can launch an interactive in-browser Gradio demo of LaVague with the following command:

```bash
lavague launch
```

??? info "Optional arguments"
    You can also use the following **optional** arguments:

    - `--url`: You can pre-populate the URL input textbox of the Gradio demo with a URL as a string here
    - `--instructions`: You can pre-populate the instruction options for the Gradio interface here with an instruction string, or list of strings
    -- `--driver`: Set this option to 'selenium' to leverage Selenium rather than the default playwright driver
    -- `--context`: Provide the name of one of our build in configuration contexts, such as 'OpenAI', 'Azure', 'Anthropic' etc.
    -- `--file_path`: Provide a path to a Python config file defining a custom ActionEngine (with the LLM, embedder, etc. of your choice)

    For more information on how to create a custom Python config file, see the [customization guide](https://docs.lavague.ai/en/latest/docs/get-started/customization/)!

You can now click on the public (if you are using Google Colab) or local URL to open your interactive LaVague demo.

!!! note "How to use Gradio demo"

    1. Click on the URL textbox and press enter. This will show a screenshot of your initial page.

    2. Select an instruction or write your own, and again click within the instruction textbox and press enter.

    Feel free to test out different URLs and instructions.

## LaVague eval

```bash
lavague eval --dataset "BigAction/the-wave-clean" --nb-data 25
```

lavague eval

dataset
nrows

??? info "Optional arguments"
    You can also use the following **optional** arguments:

    -- `--dataset`: Name of evaluation dataset slug to download from HuggingFace such as 'BigAction/the-wave-clean'
    -- `--nrows`: Number of rows of the dataset to test to be set based on your needs
    -- `--driver`: Set this option to 'selenium' to leverage Selenium rather than the default playwright driver
    -- `--context`: Provide the name of one of our build in configuration contexts, such as 'OpenAI', 'Azure', 'Anthropic' etc.
    -- `--file_path`: Provide a path to a Python config file defining a custom ActionEngine (with the LLM, embedder, etc. of your choice)

### Support

If you have any further questions, join us on the LaVague Discord [here](https://discord.com/invite/SDxn9KpqX9).