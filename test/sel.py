

from selenium.webdriver.common.by import By

import pytest
import time
from pages.homepage import HomePage
from pages.product import ProductPage






def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is("Samsung galaxy s6")
    time.sleep(2)
    title = browser.find_element(By.CSS_SELECTOR, value="h2")
    assert title.text == "Samsung galaxy s6"


def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    #browser.get("https://www.demoblaze.com/")
   # monitor_link = browser.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
    homepage.click_monitor()
    time.sleep(5)
    homepage.check_products_count(2)
    #monitor_link.click()
    #monitors = browser.find_elements(By.CSS_SELECTOR, value='.card')
    #assert len(monitors) == 2

