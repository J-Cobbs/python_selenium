import unittest
from selenium import webdriver
import time

class Checkboxes(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.checkboxes_url = self.base_url + 'checkboxes'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_first_checkbox(self):
        # checking if first checkbox is selected
        first_checkbox = '//*[@id="checkboxes"]/input[1]'
        driver = self.driver

        driver.get(self.checkboxes_url)
        checkbox_one = driver.find_element_by_xpath(first_checkbox)
        checkbox_one.click()
        print(checkbox_one.is_selected())

    def test_second_checkbox(self):
        # checking if second checkbox is not selected
        # by default second checkbox is selected so I had to click on it
        second_checkbox = '//*[@id="checkboxes"]/input[2]'
        driver = self.driver

        driver.get(self.checkboxes_url)
        checkbox_two = driver.find_element_by_xpath(second_checkbox)
        checkbox_two.click()
        print(checkbox_two.is_selected())