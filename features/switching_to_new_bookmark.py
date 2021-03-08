import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time


class NewWindow(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.new_url = self.base_url + 'windows'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_window_switch(self):
        click_here_btn_path = '//*[@id="content"]/div/a'
        header_path = '/html/body/div/h3'
        expected_text_in_header = 'New Window'
        driver = self.driver
        driver.get(self.new_url)

        window_before = driver.current_url
        print(window_before)
        btn_click_here = driver.find_element_by_xpath(click_here_btn_path).click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        current_url = driver.current_url
        print(current_url)
        time.sleep(1)
        message = driver.find_element_by_xpath(header_path).text
        self.assertEqual(expected_text_in_header, message,
                          f'Message should say: {message}')
        print(message)

    def tearDown(self):
        self.driver.quit()