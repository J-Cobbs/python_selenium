import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class Slider(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.slider_url = self.base_url + 'horizontal_slider'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_slider(self):
        slider_path = '//*[@id="content"]/div/div/input'
        slider_value_path = '//*[@id="range"]'
        driver = self.driver
        driver.get(self.slider_url)

        slider = driver.find_element_by_xpath(slider_path)
        move = ActionChains(driver)
        move.click_and_hold(slider).move_by_offset(20, 0).release().perform()
        time.sleep(1)
        value = driver.find_element_by_xpath(slider_value_path).text
        print('Slider moved to: ' + value)


    def tearDown(self):
        self.driver.quit()