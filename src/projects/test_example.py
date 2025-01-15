import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.baseclass import BaseClass

@pytest.mark.usefixtures('android_driver')
class TestExample:

    def test_web(self, android_driver):
        driver = android_driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Connections"]'))).click()

    def test_anotherThing(self, android_driver):
        driver = android_driver
        wait = WebDriverWait(driver, 10)
        el1 = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.Switch[@content-desc="Airplane mode"]')))
        assert el1.get_attribute('checked') is not True
        print("hello world")
    
    
