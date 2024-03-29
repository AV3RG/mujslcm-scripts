import time

from prettytable import PrettyTable
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

ATTENDANCE_URL = "https://mujslcm.jaipur.manipal.edu:122/Student/Academic/AttendanceSummaryForStudent"


def gather_attendance(browser):
    print("Loading attendance...")
    browser.get(ATTENDANCE_URL)
    WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.ID, "kt_ViewTable")))
    table = browser.find_element("id", "kt_ViewTable")
    table_heads = (table.find_element("tag name", "thead").find_element("tag name", "tr")
                   .find_elements("tag name", "th"))
    display = PrettyTable()
    display.field_names = [head.text for head in table_heads]
    print(display.field_names)
    table_rows = table.find_elements("tag name", "tr")
    for row in table_rows:
        cols = row.find_elements("tag name", "td")
        array = []
        for col in cols:
            array.append(col.text)
        if len(array) == 0:
            continue
        print(array)
        display.add_row(array)
    print(display)
