import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class IFrame(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.i_frame_url = self.base_url + 'frames'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_pop_up_ad(self):
        i_frame_link_path = '//*[@id="content"]/div/ul/li[2]/a'
        header_path = '//*[@id="content"]/div/h3'
        expected_header_text = 'An iFrame containing the TinyMCE WYSIWYG Editor'
        frame_path = '//*[@id="tinymce"]'
        driver = self.driver

        driver.get(self.i_frame_url)
        i_frame_link = driver.find_element_by_xpath(i_frame_link_path).click()
        header = driver.find_element_by_xpath(header_path).text
        self.assertEqual(expected_header_text, header,
                         f'Expected header should be --> {header}')
        driver.switch_to.frame('mce_0_ifr')
        frame = driver.find_element_by_xpath(frame_path).clear()
        frame = driver.find_element_by_xpath(frame_path).send_keys('Fancy text goes here')
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()