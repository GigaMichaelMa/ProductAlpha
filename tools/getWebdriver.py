from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

SUPPORTEDBROWSERS = ["chromeium", "firefox"]

# I don't know why the linter thinks this is a syntax error - it literally runs just fine lmao


def getDriver(whichBrowser="chromeium"):
    match whichBrowser:
        case "chromeium":
            return webdriver.Chrome(service=ChromiumService(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        case "firefox":
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    raise Exception(
        "Browser not found! Currently supported browsers are %s" % SUPPORTEDBROWSERS)
    return ""
