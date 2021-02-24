import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class DynamicLoading(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.dynamic_loading_url = self.base_url + 'dynamic_loading'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_dynamic_loading(self):
        example_one_path = '//*[@id="content"]/div/a[1]'
        start_btn_path = '//*[@id="start"]/button'
        message_path = '//*[@id="finish"]/h4'
        driver = self.driver

        driver.get(self.dynamic_loading_url)
        example_one = driver.find_element_by_xpath(example_one_path).click()
        start_btn = driver.find_element_by_xpath(start_btn_path).click()
        element = driver.find_element_by_xpath(message_path)
        element_expected = webdriver.support.expected_conditions.text_to_be_present_in_element(element,
                                                                                               'Hello World!').text
        print(element_expected)

    def tearDown(self):
        self.driver.quit()
