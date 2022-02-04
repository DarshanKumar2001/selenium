import time
import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service("C:/Users/DARSHAN/Desktop/Placement-webapp-using-Django-master/chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://127.0.0.1:8000/")
driver.find_element(By.CSS_SELECTOR,"#navbarBasicExample > div.buttons > a.button.is-light.is-danger > strong").click()
print(driver.title)
driver.find_element(By.NAME,'username').send_keys(data.name)
time.sleep(1)
driver.find_element(By.NAME,'password').send_keys(data.password)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"body > div > div.tile.is-ancestor > div:nth-child(2) > div > form > button > strong").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#button1 > strong").click()
driver.find_element(By.CSS_SELECTOR,"#events > div > div > article > div > div > div > a > button > strong").click()
driver.find_element(By.NAME,'phoneno').send_keys(data.mobile_no)
time.sleep(5)
driver.find_element(By.NAME,'event').send_keys(data.event_name)
time.sleep(5)
driver.find_element(By.NAME,'eventid').send_keys(data.event_id)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"body > div > div.tile.is-ancestor > div:nth-child(2) > div > form > button").click()
print("Test Successfull")
driver.quit()