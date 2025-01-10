from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

browser = webdriver.Chrome(options=options)
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit")