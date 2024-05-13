# LaVague Quick Tour

In this quick tour, we'll show you how to:

- Get setup with the LaVague framework
- Use it's basic components
- Build and run a simple application


This quick tour is also available as a [notebook on Google Colab](https://colab.research.google.com/github/lavague-ai/lavague/blob/main/docs/docs/get-started/notebooks/quick-tour.ipynb)


## Setup
To install LaVague simply run

```bash
pip install lavague
```

This will install all necessary dependencies and drivers to start using our Large Action Model framework to automate your tasks. 

## Basic Components

### Drivers
Drivers are responsible for taking control of a browser. They require a base URL which they will load first.
To use Playwright you can do: 
```py
from lavague.drivers.playwright import PlaywrightDriver
URL = "https://news.ycombinator.com"
driver = PlaywrightDriver(URL)
```
At the moment we support two well-known frameworks for browser automation: Playwright and Selenium. 


### Contexts
Contexts define the LLM used by our ActionEngine to generate code for the *Driver* to execute
To use the OpenAI context with default parameters you can do:

```py
from lavague.contexts.apis.openai_api import OpenaiContext
config = OpenaiContext.from_defaults()
```
To learn more about all Contexts we currently support, check out our Integrations page. 

### ActionEngine
The ActionEngine orchestrates everything. It is initialized from a Driver and a Context. 
It can take a natural language prompt and generate a browser action from it. 

```py
from lavague import ActionEngine
action_engine = ActionEngine.from_context(driver, config)
action = action_engine.get_action("Enter LaVague in the search bar and then press enter")
exec(action)
```
https://colab.research.google.com/github/lavague-ai/lavague/blob/main/docs/docs/get-started/quick-tour-notebook/quick-tour.ipynb

## Building a simple application with LaVague
Putting all three basic components together we can build a simple application that executes several actions starting from a given URL. 

```py
from lavague.drivers.playright import PlaywrightDriver
from lavague.contexts.apis.openai_api import OpenaiContext
from lavague import ActionEngine

URL = "https://news.ycombinator.com"

driver = PlaywrightDriver(URL)
config = OpenaiContext.from_defaults()
action_engine = ActionEngine.from_context(driver, config)
action = action_engine.get_action("Enter LaVague in the search bar and then press enter")
action.exec_code()

action = action_engine.get_action("Click the first link from the search results")
action.exec_code()
```

You could also list all instructions and execute them sequentially
```py
instructions = ["Click on the second link in the nav bar", 
                "scroll down 300px", 
                "Enter LaVague in the search bar"]

for instruction in instructions:
    action = action_engine.get_action(instruction)
    action.exec_code()
    time.sleep(1)
```



## Support

If you have any further questions, join us on the LaVague Discord [here](https://discord.com/invite/SDxn9KpqX9).