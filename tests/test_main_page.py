import time

from pages.main_page import MainPage
from pages.product_page import ProductPage


def test1(browser):
    main_page = MainPage(browser)
    main_page.open_page()
    main_page.find_element_by_link('Samsung galaxy s6').click()
    product_page = ProductPage(browser)
    result = product_page.elem_is_displayed('h2.name')
    assert result
    text = product_page.elem_text('h2.name')
    print(text)
    assert text == 'Samsung galaxy s6'


def test_monitor(browser):
    main_page = MainPage(browser)
    main_page.open_page()
    main_page.find_element_by_link('Monitors').click()
    time.sleep(2)
    product_page = ProductPage(browser)
    res = product_page.find_length('.card')
    assert res == 2
