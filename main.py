from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import roman

load_dotenv()

USERNAME = f"{os.getenv('NAME')}.{os.getenv('REGISTRATION_NUMBER')}".lower()
print(USERNAME)
PASSWORD = os.getenv("PASSWORD")

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

LOGIN_URL = "https://mujslcm.jaipur.manipal.edu:122/Home/Index"


def login():
    driver.get(LOGIN_URL)
    driver.find_element("id", "txtUserName").send_keys(USERNAME)
    driver.find_element("id", "txtPassword").send_keys(PASSWORD)
    driver.find_element("id", "login_submitStudent").click()


login()

INTERNAL_MARKS_URL = "https://mujslcm.jaipur.manipal.edu:122/Student/Academic/InternalMarkForStudent"


def select_semester():
    driver.get(INTERNAL_MARKS_URL)
    semester = int(input("Enter semester: "))
    semester = roman.toRoman(semester)
    semesterDropdown = Select(driver.find_element("id", "ddlSemester"))
    semesterDropdown.select_by_value(semester)
    driver.find_element("id", "btnSearch").click()


def get_marks():
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        print("No record found")
        return
    except TimeoutException:
        print("Loading marks...")
    table = driver.find_element("id", "kt_ViewTable")
    if table is None:
        print("No marks found")
        return
    print("Subject Code Subject Name Internal Marks External Marks Total Marks")
    rows = table.find_elements("tag name", "tr")
    for row in rows:
        cols = row.find_elements("tag name", "td")
        for col in cols:
            print(col.text, end=" ")
        print()


select_semester()
get_marks()
