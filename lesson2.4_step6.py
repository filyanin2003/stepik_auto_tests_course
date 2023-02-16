from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    browser.get("http://suninjuly.github.io/cats.html")
    browser.maximize_window()

    button_btn = browser.find_element(By.ID, ".button")
    button_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()