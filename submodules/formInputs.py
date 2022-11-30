import pyautogui


def mapInputNames2Elements(driver):
    # Not able to work on this without some way of figuring out what inputs are related to the application and which ones are just part of the site itself
    return ""


def strictInput(element, thing2Type):
    for char in thing2Type:
        element.send_keys(char)


def fileInput(element, filePath):
    element.click()
    pyautogui.write(filePath)
    pyautogui.press('enter')
