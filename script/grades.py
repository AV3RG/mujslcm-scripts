from prettytable import PrettyTable

GRADES_URL = "https://mujslcm.jaipur.manipal.edu:122/Student/Academic/CGPAGPAForStudent"


def gather_grades(browser):
    browser.get(GRADES_URL)
    table = browser.find_element("id", "kt_ViewTable")
    table_heads = (table.find_elements("tag name", "thead").find_element("tag name", "tr")
                   .find_elements("tag name", "th"))
    display = PrettyTable()
    display.field_names = [head.text for head in table_heads]
    table_rows = table.find_elements("tag name", "tr")
    for row in table_rows:
        cols = row.find_elements("tag name", "td")
        array = []
        for col in cols:
            array.append(col.text)
        display.add_row(array)
    print(display)
