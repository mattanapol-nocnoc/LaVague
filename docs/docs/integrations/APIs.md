# APIs

We provide integrations with many remote API providers such as OpenAI, HuggingFace or Anthropic through our *Contexts* module. 

We use LlamaIndex for underlying API queries and as such we follow their supported models and their naming conventions for API keys. 

## Using Contexts

Contexts define the underlying Large Language Model API used by our ActionEngine to generate code for the *driver* to execute.

Before initializing the ActionEngine, you can import a context (here with default parameters):


```py
from lavague.contexts.anthropic import AnthropicContext

context = AnthropicContext.from_defaults()
action_engine = ActionEngine.from_context(driver, context)
```


## API Credentials
When using remote APIs, you usually need authentication credentials in the form of an API key.

We use environment variables to find API keys, here's how you can set environment variables: 

Setting up a **local** environment variable varies based your OS. Checkout [this guide](https://www.twilio.com/en-us/blog/how-to-set-environment-variables-html) if you're having issues. 

You can also set environment variables directly in your code (useful when running in Google Colab):
```py
import os
os.environ['ANTHROPIC_API_KEY'] = # ADD YOUR KEY HERE
```


## Using the CLI with a context
!!! note "Coming soon"
    You will soon be able to use the CLI `demo` and `eval` tools with a custom context. 

To change the context used by the CLI, you can use the `--context` argument
```bash
lavague demo --context "AnthropicContext"
```

## Support

If you have any further questions, join us on the LaVague Discord [here](https://discord.com/invite/SDxn9KpqX9).