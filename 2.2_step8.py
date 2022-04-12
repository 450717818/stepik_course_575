from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = 'https://suninjuly.github.io/file_input.html'
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'bio.txt')
    file_path = '/dev/null'
    browser = webdriver.Firefox()
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    browser.find_element(By.NAME, 'lastname').send_keys('Petrov')
    browser.find_element(By.NAME, 'email').send_keys('ivan@petrov.ru')
    browser.find_element(By.CSS_SELECTOR, 'input#file').send_keys(file_path)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
finally:
    time.sleep(10)
    browser.quit()

