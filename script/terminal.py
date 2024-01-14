import os

from dotenv import load_dotenv
from inquirer import Text, Password, List

from util.prompter import prompt


def gather_inputs():
    def check_env_exist():
        load_dotenv()
        exists = os.getenv("NAME") is not None and os.getenv("REGISTRATION_NUMBER") is not None and os.getenv(
            "PASSWORD") is not None
        if not exists:
            print("""
                Few environment variables are missing. 
                Please create a .env file in the root directory of this project and add the following variables:
                NAME
                REGISTRATION_NUMBER
                PASSWORD
                
                The program will continue for now, asking for these inputs.
            """)

    def get_name():
        return os.getenv("NAME") or prompt(Text("username", message="Please enter your name: "))

    def get_registration_number():
        return os.getenv("REGISTRATION_NUMBER") or prompt(Text(
                "registration_number",
                message="Please enter your registration number: ",
                validate=lambda _, x: len(x) == 9 and x.isdigit()
            ))

    def get_password():
        return os.getenv("PASSWORD") or prompt(Password("password", message="Please enter your password: "))

    def get_browser():
        return prompt(List(
                name="browser",
                message="Please select your browser",
                choices=[
                    "Firefox",
                    "Chrome"
                ],
                default="Firefox",
                carousel=True
            ))

    def get_headless_option():
        return prompt(List(
                name="headless",
                message="Do you want to run the browser in headless mode?",
                choices=[
                    "Yes (recommended)",
                    "No"
                ],
                default="Yes (recommended)",
                carousel=True
            ))

    check_env_exist()
    name = get_name()
    registration_number = get_registration_number()
    password = get_password()
    browser = get_browser()
    headless = get_headless_option()

    return {
        "username": f"{name}.{registration_number}".lower(),
        "name": name,
        "registration_number": registration_number,
        "password": password,
        "browser": browser,
        "headless": headless
    }
