from selenium import webdriver
from selenium.webdriver.common.by import By


def get_link():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    submit = driver.find_element(By.CSS_SELECTOR, '#login-button')

    if username is None and password is None and submit is None:
        return ('')
    else:
        return ('Элементы найдены')


print(get_link())
