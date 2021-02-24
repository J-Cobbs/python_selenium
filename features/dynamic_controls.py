import unittest
from selenium import webdriver
import time

class DynamicControls(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.controls_url = self.base_url + 'dynamic_controls'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_add_delete_checkbox(self):
        message_path = '//*[@id="message"]'
        message_expected = "It's gone!"
        message_expected_two = "It's back!"
        checkbox_path = '//*[@id="checkbox"]/input'
        checkbox_path_two = '//*[@id="checkbox"]'
        add_remove_btn_path = '//*[@id="checkbox-example"]/button'
        driver = self.driver

        # by default, checkbox must be removed, so I will remove it first
        driver.get(self.controls_url)
        checkbox = driver.find_element_by_xpath(checkbox_path).click()
        add_remove_btn = driver.find_element_by_xpath(add_remove_btn_path).click()
        time.sleep(3)
        message = driver.find_element_by_xpath(message_path).text
        self.assertEqual(message_expected, message,
                         f'Message should say: {message}')
        print(message)

        # I will continue with adding it back
        add_remove_btn = driver.find_element_by_xpath(add_remove_btn_path).click()
        time.sleep(3)
        message = driver.find_element_by_xpath(message_path).text
        self.assertEqual(message_expected_two, message,
                         f'Message should say: {message}')
        print(message)

        # and removing it again
        checkbox_two = driver.find_element_by_xpath(checkbox_path_two).click()
        add_remove_btn = driver.find_element_by_xpath(add_remove_btn_path).click()
        time.sleep(3)
        message = driver.find_element_by_xpath(message_path).text
        self.assertEqual(message_expected, message,
                         f'Message should say: {message}')
        print(message)

    def test_enable_disable_field(self):
        enable_disable_btn_path = '//*[@id="input-example"]/button'
        input_field_path = '//*[@id="input-example"]/input'
        message_path = '//*[@id="message"]'
        message_expected = "It's enabled!"
        message_expected_two = "It's disabled!"
        driver = self.driver

        # by default, field is disabled, so I will enable it first, write something and disable it back
        driver.get(self.controls_url)
        enable_disable_btn = driver.find_element_by_xpath(enable_disable_btn_path).click()
        time.sleep(3)
        message = driver.find_element_by_xpath(message_path).text
        self.assertEqual(message_expected, message,
                         f'Message should say: {message}')
        print(message)
        input_field = driver.find_element_by_xpath(input_field_path).send_keys("Hello World")
        enable_disable_btn = driver.find_element_by_xpath(enable_disable_btn_path).click()
        time.sleep(3)
        message = driver.find_element_by_xpath(message_path).text
        self.assertEqual(message_expected_two, message,
                         f'Message should say: {message}')
        print(message)

        #who don't like time.sleep() ? :)

    def tearDown(self):
        self.driver.quit()