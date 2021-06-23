import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBukalapaklogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bukalapaklogin(self):
    # Test name: bukalapaklogin
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://www.bukalapak.com/")
    # 2 | setWindowSize | 1382x744 | 
    self.driver.set_window_size(1382, 744)
    # 3 | click | css=.te-header-login > .pr-4 | 
    self.driver.find_element(By.CSS_SELECTOR, ".te-header-login > .pr-4").click()
    # 4 | click | id=user_session_username | 
    self.driver.find_element(By.ID, "user_session_username").click()
    # 5 | type | id=user_session_username | alamat email kamu
    self.driver.find_element(By.ID, "user_session_username").send_keys("alamat email kamu")
    # 6 | click | id=user_session_password | 
    self.driver.find_element(By.ID, "user_session_password").click()
    # 7 | type | id=user_session_password | isikan password kamu
    self.driver.find_element(By.ID, "user_session_password").send_keys("isikan password kamu")
    # 8 | click | css=.remember-me-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".remember-me-label").click()
    # 9 | click | name=commit | 
    self.driver.find_element(By.NAME, "commit").click()
    # 11 | close |  | 
    self.driver.close()
  
