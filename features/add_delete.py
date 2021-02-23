import unittest
from selenium import webdriver
import time

class AddRemoveElement(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.remove_url = self.base_url + 'add_remove_elements/'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_add_element(self):
        add_btn = '//*[@id="content"]/div/button'
        driver = self.driver

        driver.get(self.remove_url)
        self.driver.find_element_by_xpath(add_btn).click()
        time.sleep(2)

    def test_delete_element(self):
        add_btn = '//*[@id="content"]/div/button'
        delete_btn = '//*[@id="elements"]/button'
        driver = self.driver

        driver.get(self.remove_url)
        self.driver.find_element_by_xpath(add_btn).click()
        time.sleep(2)
        delete_btn_visibility = driver.find_element_by_xpath(delete_btn)
        print(delete_btn_visibility.is_displayed())
        self.driver.find_element_by_xpath(delete_btn).click()
        time.sleep(2)
        # could not find anything better than sleep