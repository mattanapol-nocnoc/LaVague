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

The `eval` command allows you to quickly evaluate the performance of LaVague's `Large Action Model` by testing the precision and recall of LaVague's LLM and retriever on a batch of instructions against ground truths contained in an evaluation dataset. We provide datasets that can be used for evaluating LaVague in our [BigAction` repo on HuggingFace](https://huggingface.co/BigAction).

The `eval` command will create a `json` file with the following data for each instruction of the evaluation dataset:

- recall_retriever: retriever recall
- precision_retriever: retriever precision
- recall_llm: LLM recall
- precision_llm: LLM precision
- retrieved_context: The context retrieved
- ground_truth_outer_html: The ground truths for the path of targetted HTML element
- retriever_time: time taken for retrieval
- llm_time: time taken for LLM query

```bash
lavague eval --dataset "BigAction/the-wave-clean" --nb-data 25
```

You can then query the data provided in the json file to investigate the performance of LaVague.

???+ "Example queries on output file"
    For example, you could get the average precision and recall of the retriever with the following code:

    ```python
    # function for printing avergae retriever recall & prevcision
    def retriever_stats(filename: str):
    import json

    # Open the file
    with open(filename, 'r') as file:
        json_data = [json.loads(line) for line in file]

    # Calculate average recall_retriever and precision_retriever
    total_recall = sum(entry['recall_retriever'] for entry in json_data)
    total_precision = sum(entry['precision_retriever'] for entry in json_data)
    average_recall = total_recall / len(json_data)
    average_precision = total_precision / len(json_data)

    # Print average values
    print("Average recall: {:.2f}".format(average_recall))
    print("Average precision: {:.2f}".format(average_precision))

    retriever_stats('openai.json')
    ```

??? info "Optional arguments"
    You can also use the following **optional** arguments:

    -- `--dataset`: Name of evaluation dataset slug to download from HuggingFace such as 'BigAction/the-wave-clean'
    -- `--nrows`: Number of rows of the dataset to test to be set based on your needs
    -- `--driver`: Set this option to 'selenium' to leverage Selenium rather than the default playwright driver
    -- `--context`: Provide the name of one of our build in configuration contexts, such as 'OpenAI', 'Azure', 'Anthropic' etc.
    -- `--file_path`: Provide a path to a Python config file defining a custom ActionEngine (with the LLM, embedder, etc. of your choice)

### Support

If you have any further questions, join us on the LaVague Discord [here](https://discord.com/invite/SDxn9KpqX9).