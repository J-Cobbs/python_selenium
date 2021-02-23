import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class ContexMenu(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.context_menu_url = self.base_url + 'context_menu'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_context_menu(self):
        box_field_path = '//*[@id="hot-spot"]'
        driver = self.driver
        # right click on the box field
        driver.get(self.context_menu_url)
        actionChains = ActionChains(driver)
        box_field = driver.find_element_by_xpath(box_field_path)
        actionChains.context_click(box_field).perform()

        # switching to alert and accepting it
        alert = driver.switch_to.alert
        msg = alert.text
        print("Alert shows following message: " + msg)
        time.sleep(1)
        alert.accept()
        print(" Clicked on the OK Button in the Alert Window")

    def tearDown(self):
        self.driver.quit()