from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.get('https://demoblaze.com/')

    def find_element_by_link(self, text):
        return self.browser.find_element(By.LINK_TEXT, text)
