from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseClass(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        # * explodes the the tuple
        return self.driver.find_element(*locator)

    def instance(cls, driver):
        return cls(driver)