import time
import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service("C:/Users/DARSHAN/Desktop/Placement-webapp-using-Django-master/chromedriver_win32 (1)/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://127.0.0.1:8000/")
driver.find_element(By.CSS_SELECTOR,"#navbarBasicExample > div.navbar-start > a:nth-child(5) > strong").click()
print(driver.title)
driver.find_element(By.NAME,'username').send_keys(data.name)
driver.find_element(By.NAME,'password').send_keys(data.password)
driver.find_element(By.CSS_SELECTOR,"body > div > div.tile.is-ancestor > div:nth-child(2) > div > form > button > strong").click()
driver.find_element(By.CSS_SELECTOR,"#navbarBasicExample > div.navbar-start > a:nth-child(5) > strong").click()
driver.find_element(By.CSS_SELECTOR,"#events > div > div > article > div > div > div > a > button > strong").click()
driver.find_element(By.NAME,'phoneno').send_keys(data.mobile_no)
driver.find_element(By.NAME,'college').send_keys(data.college_name)
driver.find_element(By.NAME,'graduation').send_keys(data.graduation_year)
driver.find_element(By.NAME,'company').send_keys(data.company_name)
driver.find_element(By.NAME,'companyid').send_keys(data.company_id)
driver.find_element(By.NAME,'profile').send_keys(data.job_profile)
driver.find_element(By.NAME,'skills').send_keys(data.skills)
driver.find_element(By.NAME,'body > div > div.tile.is-ancestor > div:nth-child(2) > div > form > div:nth-child(11) > div > label > span.file-cta > span.file-label').send_keys()
driver.find_element(By.CSS_SELECTOR,"body > div > div.tile.is-ancestor > div:nth-child(2) > div > form > button > strong").click()