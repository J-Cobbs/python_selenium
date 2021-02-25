import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class PopUpModal(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.entry_ad_url = self.base_url + 'entry_ad'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_pop_up_ad(self):
        pop_up_message_path = '//*[@id="modal"]/div[2]/div[2]/p/text()'
        close_pop_up_btn_path = '#modal > div.modal > div.modal-footer > p'
        modal_path = '//*[@id="modal"]/div[2]'
        restart_pop_up_modal_path = '//*[@id="restart-ad"]'
        driver = self.driver

        driver.get(self.entry_ad_url)
        message_expected = webdriver.support.expected_conditions.text_to_be_present_in_element(pop_up_message_path,
                                                                                               "It's commonly used to encourage a user to take an action (e.g., give their e-mail address to sign up for something or disable their ad blocker).").text
        print(message_expected)
        # modal appears, switch to modal and then click on close
        modal = webdriver.support.expected_conditions.frame_to_be_available_and_switch_to_it(modal_path)
        time.sleep(2)
        close_btn = driver.find_element_by_css_selector(close_pop_up_btn_path).click()

        # enabling modal again, and again closing it
        re_enable = driver.find_element_by_xpath(restart_pop_up_modal_path).click()
        message_expected = webdriver.support.expected_conditions.text_to_be_present_in_element(pop_up_message_path,
                                                                                               "It's commonly used to encourage a user to take an action (e.g., give their e-mail address to sign up for something or disable their ad blocker).").text
        print('Again same message: ' + message_expected)
        time.sleep(1)
        close_btn = driver.find_element_by_css_selector(close_pop_up_btn_path).click()

    def tearDown(self):
        self.driver.quit()