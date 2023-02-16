from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.maximize_window()

    #button_btn = browser.find_element(By.CSS_SELECTOR, ".trollface")
    time.sleep(2)
    button_btn = browser.find_element(By.TAG_NAME, "button")
    button_btn.click()
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()