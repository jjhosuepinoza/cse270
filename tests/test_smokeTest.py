# Generated by Selenium IDE
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

class TestSmokeTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_homePage(self):
    self.driver.get("http://127.0.0.1:8000/teton/1.6/index.html")
    self.driver.set_window_size(1552, 832)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    element = self.driver.find_element(By.LINK_TEXT, "Join")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".header-top").click()
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    self.driver.find_element(By.CSS_SELECTOR, ".join-wizard-main").click()
  
  def test_adminPage(self):
    self.driver.get("http://127.0.0.1:8000/teton/1.6/admin.html")
    self.driver.set_window_size(782, 823)
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").send_keys("ggfdsfg")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("dfasdfasd")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".errorMessage").text == "Invalid username and password."
    self.driver.find_element(By.CSS_SELECTOR, ".footer-content").click()
  
  def test_directoryPage(self):
    self.driver.get("http://127.0.0.1:8000/teton/1.6/directory.html")
    self.driver.set_window_size(784, 817)
    self.driver.find_element(By.ID, "directory-grid").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9)")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "directory-list").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, "#hamburger-equiv > img").click()
    self.driver.find_element(By.LINK_TEXT, "Join").click()
  
  def test_joinPage(self):
    self.driver.get("http://127.0.0.1:8000/teton/1.6/join.html")
    self.driver.set_window_size(782, 823)
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("Javier")
    self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").click()
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.NAME, "lname").send_keys("Espinaza")
    self.driver.find_element(By.NAME, "bizname").click()
    self.driver.find_element(By.NAME, "bizname").send_keys("Two")
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("Manager")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
  
