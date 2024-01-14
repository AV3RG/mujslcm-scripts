from selenium.webdriver.chrome.webdriver import WebDriver

LOGIN_URL_ENTRY = "https://mujslcm.jaipur.manipal.edu:122/Home/Index"
LOGIN_URLS = [
    LOGIN_URL_ENTRY,
    "https://mujslcm.jaipur.manipal.edu:122/"
]


def login_user(browser: WebDriver, username, password):
    browser.get(LOGIN_URL_ENTRY)
    browser.find_element("id", "txtUserName").send_keys(username)
    browser.find_element("id", "txtPassword").send_keys(password)
    browser.find_element("id", "login_submitStudent").click()
    if browser.current_url in LOGIN_URLS:
        raise Exception("Invalid credentials")
