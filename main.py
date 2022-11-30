from tools.getWebdriver import getDriver
import submodules.formInputs as fi
from selenium.webdriver.common.by import By

driver = getDriver("firefox")
driver.get("https://boards.greenhouse.io/duolingo/jobs/6444746002#app")


# # beyond here is test code


# first_name = driver.find_element(
#     By.XPATH, "/html/body/div[1]/div/div[1]/div[4]/form/div[1]/div[4]/input")
# print(first_name)
# fi.strictInput(first_name, "Chad Bruher")


# filePath = "C:\\Users\\..."
# resumeInput = driver.find_element(
#     By.XPATH, "/html/body/div[1]/div/div[1]/div[4]/form/div[1]/div[10]/fieldset/div/div[3]/button[1]")
# fi.fileInput(resumeInput, filePath)
