from prettytable import PrettyTable

from selenium.webdriver.support.select import Select
from util.prompter import prompt
from inquirer.questions import List
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

INTERNAL_MARKS_URL = "https://mujslcm.jaipur.manipal.edu:122/Student/Academic/InternalMarkForStudent"


def gather_internal_marks(browser):
    print("Loading internal marks...")
    browser.get(INTERNAL_MARKS_URL)

    def select_semester():
        select_tag = browser.find_element("id", "ddlSemester")
        option_tags = select_tag.find_elements("tag name", "option")
        options = []
        for option in option_tags:
            options.append((option.get_attribute("value"), option.text))

        print(list(map(lambda x: x[1], options)))
        selected_option = prompt(List(
            name="semester",
            message="Please select your semester",
            choices=list(map(lambda x: x[1], options)),
            carousel=True
        ))["semester"]
        selected_option_value = next((x for x in options if x[1] == selected_option), None)[0]
        select_clickable = Select(select_tag)
        select_clickable.select_by_value(selected_option_value)
        browser.find_element("id", "btnSearch").click()

    def get_marks():
        try:
            WebDriverWait(browser, 3).until(ec.alert_is_present(),
                                           'Timed out waiting for PA creation ' +
                                           'confirmation popup to appear.')

            alert = browser.switch_to.alert
            alert.accept()
            print("No record found")
            return
        except TimeoutException:
            print("Loading marks...")
        table = browser.find_element("id", "kt_ViewTable")
        if table is None:
            print("No marks found")
            return
        table_heads = (table.find_element("tag name", "thead").find_element("tag name", "tr")
                       .find_elements("tag name", "th"))
        display = PrettyTable()
        display.field_names = [head.text for head in table_heads]
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

    select_semester()
    get_marks()
