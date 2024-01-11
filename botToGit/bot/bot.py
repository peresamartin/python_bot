from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions
import time
import random

file = open("acc.txt", "r")
line = file.readline().split(" ")
myAcc = line[0]
myPass = line[1]

options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://hybe.com/")


time.sleep(10)
elem = driver.find_element(By.XPATH, "//div[@id='announcement-bar']/..//button/span[contains(text(), 'Log in')]/..")
elem.click()

time.sleep(4)
eMail = driver.find_element(By.ID, "email")
eMail.send_keys(myAcc)

time.sleep(4)
password = driver.find_element(By.ID, "password")
password.send_keys(myPass)

time.sleep(1)
btnLogin = driver.find_element(By.XPATH, "//form/button")
btnLogin.click()
time.sleep(7)
i=0
while True:
    print(i)
    chat = driver.find_element(By.XPATH, "//div[contains(@id,'popover-trigger')]/textarea")
    chat.click()


    # button = driver.find_element(By.XPATH, "//button[contains(text(), 'Enter the Rain Pool')]")

    button = WebDriverWait(driver, 5000000).until(lambda x: x.find_element
                                        (By.XPATH, "//button[contains(text(), 'Enter the Rain Pool')]"))
    

    sleep = random.randint(5,80)
    time.sleep(sleep)

    button.click()
    inputText = random.choice(["w", "gl", "Pog", "W"])
    chat.send_keys(inputText)
    time.sleep(0.5)
    chat.send_keys(Keys.ENTER)
    i=i+1
    time.sleep(200)