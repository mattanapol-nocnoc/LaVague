# Selenium Integration

While LaVague uses Playwright by default which offers easier driver installation, we also offer built-in support for Selenium and hope to support more driver integrations in the future.

In this section, we'll provide guidance on how to get started using LaVague with Selenium.

### Selenium Driver installation

If you haven't already, you will need to install the driver, a browser-specific implementation of the [Webdriver API](https://www.selenium.dev/documentation/webdriver/), which Selenium will leverage to automate actions on the web.

For LaVague, by default, we expect to find the Chrome webdriver and Chrome binaries in your home repo. For MacOS or Linux users (on Debian-based distributions), we provide a script to install these binaries and place them in the expected location.

For Linux users:
```bash
wget https://raw.githubusercontent.com/lavague-ai/LaVague/main/selenium-setup-scripts/selenium-linux.sh
bash selenium-linux.sh
```

For MacOS users:
```bash
wget https://raw.githubusercontent.com/lavague-ai/LaVague/main/selenium-setup-scripts/selenium-macos.sh
bash selenium-macos.sh
```

For guidance on installing chromedriver in Windows see [instructions here](https://chromedriver.chromium.org/getting-started).

!!! info "changing default paths or drivers"
    If you want to modify the paths or navigator used by LaVague in our default Selenium driver, you will need to modify the [Selenium driver package](https://github.com/lavague-ai/LaVague/blob/big-refactor/lavague-integrations/drivers/lavague-drivers-selenium/lavague/drivers/selenium/base.py) and install this package from your locally modified version.

### Using LaVague with Selenium

To use the LaVague library with Selenium, you will need to import our SeleniumDriver object which you can initialize with the URL of the website you wish to perform actions on.

```python
from lavague.drivers.selenium import SeleniumDriver
from lavague.contexts.openai import OpenaiContext
from lavague.core import ActionEngine

selenium_driver = SeleniumDriver("https://news.ycombinator.com")
openai_context = OpenaiContext.from_defaults()
action_engine = ActionEngine.from_context(selenium_driver, openai_context)
action = action_engine.get_action("Enter hop inside the search bar and then press enter")
print(action)
```



