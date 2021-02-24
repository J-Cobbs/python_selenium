import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class DynamicContent(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.content_url = self.base_url + 'dynamic_content'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_first_paragraph(self):
        first_text_path = '//*[@id="content"]/div[1]/div[2]'
        driver = self.driver

        # checking if text is same than before
        driver.get(self.content_url)
        first_text_before = driver.find_element_by_xpath(first_text_path).text
        # time.sleep(2)
        driver.refresh()
        first_text_after = driver.find_element_by_xpath(first_text_path).text
        self.assertNotEqual(first_text_before, first_text_after)
        print('First text before ' + first_text_before)
        print('First text after ' + first_text_after)

    def test_second_paragraph(self):
        second_text_path = '//*[@id="content"]/div[3]/div[2]'
        driver = self.driver

        driver.get(self.content_url)
        third_text_before = driver.find_element_by_xpath(second_text_path).text
        driver.refresh()
        third_text_after = driver.find_element_by_xpath(second_text_path).text
        self.assertNotEqual(third_text_before, third_text_after)
        print('Second text before ' + third_text_after)
        print('Second text after ' + third_text_after)

    def test_third_paragraph(self):
        third_text_path = '//*[@id="content"]/div[3]/div[2]'
        driver = self.driver

        driver.get(self.content_url)
        second_text_before = driver.find_element_by_xpath(third_text_path).text
        driver.refresh()
        second_text_after = driver.find_element_by_xpath(third_text_path).text
        self.assertNotEqual(second_text_before, second_text_after)
        print('Third text before ' + second_text_before)
        print('Third text after ' + second_text_after)


    def tearDown(self):
        self.driver.quit()