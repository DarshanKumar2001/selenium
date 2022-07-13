import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import data
global driver
class TestRegister():
    @pytest.fixture()
    def setup(self):
        global driver
        #executes in every test
        self.driver=webdriver.Chrome(executable_path="C:/Users/DARSHAN/Desktop/Placement-webapp-using-Django-master/chromedriver_win32 (1)/chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()
    def test_new_event(self, setup):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element(By.CSS_SELECTOR,"#navbarBasicExample > div.buttons > a.button.is-light.is-danger > strong").click()
        self.driver.find_element(By.NAME, 'username').send_keys(data.name)
        time.sleep(5)
        self.driver.find_element(By.NAME, 'password').send_keys(data.password)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,"body > div > div.tile.is-ancestor > div:nth-child(2) > div > form > button > strong").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "#button1 > strong").click()
        self.driver.find_element(By.CSS_SELECTOR,"#events > div > div > article > div > div > div > a > button > strong").click()
        self.driver.find_element(By.NAME, 'phoneno').send_keys(data.mobile_no)
        time.sleep(2)
        self.driver.find_element(By.NAME, 'event').send_keys(data.event_name)
        time.sleep(2)
        self.driver.find_element(By.NAME, 'eventid').send_keys(data.event_id)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"body > div > div.tile.is-ancestor > div:nth-child(2) > div > form > button").click()

