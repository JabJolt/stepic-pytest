""" Lesson 1.6 """
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import string

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')


def task_1():

    LINK = "http://suninjuly.github.io/simple_form_find_task.html"
    value1: str = "input"
    value2: str = "last_name"
    value3: str = "form-control.city"


    try:
        browser = webdriver.Chrome(options=options)
        browser.get(LINK)

        input1 = browser.find_element(By.TAG_NAME, value1)
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, value2)
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, value3)
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

# task_1()

def task_2():

    import math

    LINK = "http://suninjuly.github.io/find_link_text"
    search_str: str = str(math.ceil(math.pow(math.pi, math.e)*10000))

    try:
        browser = webdriver.Chrome(options=options)
        browser.get(LINK)

        link = browser.find_element(By.PARTIAL_LINK_TEXT, search_str)
        link.click()
        
        value1: str = "input"
        value2: str = "last_name"
        value3: str = "form-control.city"

        input1 = browser.find_element(By.TAG_NAME, value1)
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, value2)
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, value3)
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()

# task_2()

def task3():

    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/huge_form.html")
        elements = browser.find_elements(By.TAG_NAME, "input")
        for element in elements:
            element.send_keys(string.ascii_uppercase[:6])

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

# task3()


def task4():

    LINK = "http://suninjuly.github.io/find_xpath_form"

    try:
        browser = webdriver.Chrome(options=options)
        browser.get(LINK)

        value1: str = "input"
        value2: str = "last_name"
        value3: str = "form-control.city"

        input1 = browser.find_element(By.TAG_NAME, value1)
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, value2)
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, value3)
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")

        button = browser.find_element(By.XPATH, '//button[@type="submit"]')
        button.click()
        

    finally:
        time.sleep(30)
        browser.quit()

# task4()



def task6():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    try: 
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(options=options)
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'Input your first name')]")
        input1.send_keys("Doggo")
        
        input2 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'Input your last name')]")
        input2.send_keys("Wuffers")

        input3 = browser.find_element(By.XPATH, "//input[contains(@placeholder,'Input your email')]")
        input3.send_keys("dogger@wufwuf.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()


# task6()

def task6_someones():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    try: 
        link = "http://suninjuly.github.io/registration2.html"
        
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR,"input[placeholder='Input your first name']")
        input1.send_keys("Upa")
        input2 = browser.find_element(By.CSS_SELECTOR,"input[placeholder='Input your last name']")
        input2.send_keys("Kovka")
        input3 = browser.find_element(By.CSS_SELECTOR,"input[placeholder='Input your email']")
        input3.send_keys("pochta@mail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(1)
        browser.quit()

task6_someones()        