from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from login import login_user
from terminal import gather_inputs


def start():
    inputs = gather_inputs()
    match inputs["browser"]:
        case "firefox":
            options = FirefoxOptions()
            if inputs["headless"]:
                options.add_argument("--headless")
            browser = webdriver.Firefox(options=options)
        case "chrome":
            options = ChromeOptions()
            if inputs["headless"]:
                options.add_argument("--headless")
            browser = webdriver.Chrome(options=options)
        case _:
            raise Exception("Invalid browser")
    try:
        login_user(browser, inputs["username"], inputs["password"])
    except Exception as e:
        print(e)
        start()


start()

