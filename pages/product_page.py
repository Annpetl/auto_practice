from selenium.webdriver.common.by import By

from pages.main_page import MainPage


class ProductPage(MainPage):

    def elem_is_displayed(self, elem):
        element = self.browser.find_element(By.CSS_SELECTOR, elem).is_displayed()
        return element

    def elem_text(self, elem):
        text = self.browser.find_element(By.CSS_SELECTOR, elem).text
        return text

    def find_length(self, elem):
        res = self.browser.find_elements(By.CSS_SELECTOR, elem)
        return len(res)

