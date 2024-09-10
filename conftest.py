import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument(' --disable-search-engine-choice-screen')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    yield driver

