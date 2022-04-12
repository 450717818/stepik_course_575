import math
from selenium import webdriver
import time


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    treasure = browser.find_element_by_css_selector("img#treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    browser.find_element_by_css_selector("input#answer").send_keys(str(y))
    browser.find_element_by_css_selector('input#robotCheckbox.check-input').click()
    browser.find_element_by_css_selector('input#robotsRule.check-input').click()
    browser.find_element_by_css_selector('button[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()

