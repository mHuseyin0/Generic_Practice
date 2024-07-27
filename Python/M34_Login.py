from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

DRIVER = webdriver.Chrome()
DRIVER.get("https://stars.bilkent.edu.tr/")

SRS: WebElement
SRS = WebDriverWait(DRIVER,10).until(EC.presence_of_element_located((By.LINK_TEXT,"SRS")))
SRS.click()

DRIVER.minimize_window()

username: WebElement
username = WebDriverWait(DRIVER,10).until(EC.presence_of_element_located((By.ID,"LoginForm_username")))

#username.clear() clears the texts inside an text entry element like textbox
username.send_keys("22203683")

password: WebElement
password = DRIVER.find_element(By.ID,"LoginForm_password")

password.send_keys("YHFR13")

from time import sleep
sleep(3)
submit = DRIVER.find_element(By.TAG_NAME,"button")

submit.click()

code = input("Please input the authentication code: ")


codeBox: WebElement
codeBox = WebDriverWait(DRIVER,10).until(EC.presence_of_element_located((By.ID,"SmsVerifyForm_verifyCode")))

codeButton = DRIVER.find_element(By.TAG_NAME,"button")

codeBox.send_keys(code)
codeButton.click()

DRIVER.fullscreen_window()
input()
#DRIVER.back() goes one step bakcwards in the history, and DRIVER.forward() goes one step forward.

