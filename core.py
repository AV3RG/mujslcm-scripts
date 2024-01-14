from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from inquirer.questions import List

from script.attendance import gather_attendance
from script.gpa import gather_grades
from script.internal_marks import gather_internal_marks
from script.login import login_user
from script.terminal import gather_inputs
from util.prompter import prompt


def start():
    inputs = gather_inputs()
    match inputs["browser"]:
        case "Firefox":
            options = FirefoxOptions()
            if inputs["headless"]:
                options.add_argument("--headless")
            browser = webdriver.Firefox(options=options)
        case "Chrome":
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

    print("Logged in successfully")
    while True:
        option = prompt(List(
            name="action",
            message="What do you want to do?",
            choices=[
                "Get attendance",
                "Get internal marks",
                "Get grades",
                "Exit"
            ],
            carousel=True
        ))["action"]
        match option:
            case "Get attendance":
                gather_attendance(browser)
            case "Get internal marks":
                gather_internal_marks(browser)
            case "Get grades":
                gather_grades(browser)
            case "Exit":
                break


start()
