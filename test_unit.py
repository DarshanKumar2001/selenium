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
    def test_loginpage(self,setup):
        self.driver.get("http://127.0.0.1:8000/login/")
        print(self.driver.title)
        self.driver.find_element(By.NAME, 'username').send_keys(data.name)
        time.sleep(1)
        self.driver.find_element(By.NAME, 'password').send_keys(data.password)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,"body > div > div.tile.is-ancestor > div:nth-child(2) > div > form > button > strong").click()
        assert self.driver.title=="Home"
    def test_homePselfageTitle(self,setup):
        self.driver.get("http://127.0.0.1:8000/register/")
        print(self.driver.title)
        self.driver.find_element(By.NAME,'username').send_keys("darshan")
        self.driver.find_element(By.NAME,'email').send_keys("dk343679@gmail.com")
        self.driver.find_element(By.NAME,'password1').send_keys("kumar@123")
        self.driver.find_element(By.NAME,'password2').send_keys("kumar@123")
        self.driver.find_element(By.CSS_SELECTOR,"body > div > div.tile.is-ancestor > div:nth-child(2) > div > form > button > strong").click()
        assert self.driver.title=="Home"
