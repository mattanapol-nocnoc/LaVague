from lavague.drivers.playwright import PlaywrightDriver
from lavague.contexts.groq import GroqContext
from lavague.core import ActionEngine

# Don't forget to export GROQ_API_KEY

# TODO script is broken and printing None

playwright_driver = PlaywrightDriver("https://news.ycombinator.com")
groq_context = GroqContext.from_defaults()
action_engine = ActionEngine.from_context(playwright_driver, groq_context)
action = action_engine.get_action("Enter hop inside the search bar and then press enter")
print(action)
