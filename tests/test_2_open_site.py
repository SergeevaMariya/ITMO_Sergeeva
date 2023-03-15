from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://demoqa.com/")

#поиск элемента                                 #локатор
# icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')

icon = driver.find_element(By.CSS_SELECTOR, '#app > header > a > img')
footer = driver.find_element(By.CSS_SELECTOR, '#app > footer > span')
button = driver.find_elements(By.CSS_SELECTOR, 'div.home-body > div > div:nth-child(1)card mt-4')

if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

if footer is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

if button is None:
    print('Элемент не найден')
else:
    print('Элемент найден')



