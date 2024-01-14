from prettytable import PrettyTable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

GPA_URL = "https://mujslcm.jaipur.manipal.edu:122/Student/Academic/CGPAGPAForStudent"


def gather_grades(browser):
    print("Loading gpa...")
    browser.get(GPA_URL)
    WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.ID, "kt_ViewTable")))
    table = browser.find_element("id", "kt_ViewTable")

    display = PrettyTable()
    head_row = list(map(lambda x: x.text, table.find_element("tag name", "thead").find_elements("tag name", "tr")[0]
                        .find_elements("tag name", "th")))
    fields = []
    for col in head_row:
        if col.startswith("Semester"):
            fields.append(f"{col} GPA")
            fields.append(f"{col} Credits")
        else:
            fields.append(col)
    display.field_names = fields
    table_rows = table.find_elements("tag name", "tr")
    for row in table_rows:
        cols = row.find_elements("tag name", "td")
        array = []
        for col in cols:
            array.append(col.text)
        if len(array) == 0:
            continue
        display.add_row(array)
    print(display)
