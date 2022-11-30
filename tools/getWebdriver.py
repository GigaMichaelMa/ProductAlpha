from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

SUPPORTEDBROWSERS = ["chrome"]

# I don't know why the linter thinks this is a syntax error - it literally runs just fine lmao


def getDriver(whichBrowser="chrome"):
    match whichBrowser:
        case "chrome":
            return webdriver.Chrome(service=ChromiumService(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    raise Exception(
        "Browser not found! Currently supported browsers are %s" % SUPPORTEDBROWSERS)
    return ""
