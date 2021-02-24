import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class ContexMenu(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.drag_drop_url = self.base_url + 'drag_and_drop'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_drag_and_drop(self):
        b_box_path = '//*[@id="column-b"]'
        a_box_path = '//*[@id="column-a"]'
        header_a_path = '//*[@id="column-a"]/header'
        header_b_path = '//*[@id="column-b"]/header'
        driver = self.driver
        actionChains = ActionChains(driver)

        # dropping box B in A box place
        driver.get(self.drag_drop_url)
        box_B = driver.find_element_by_xpath(b_box_path)
        box_A = driver.find_element_by_xpath(a_box_path)
        header_a = driver.find_element_by_xpath(header_a_path).text
        header_b = driver.find_element_by_xpath(header_b_path).text
        drop_place = actionChains.drag_and_drop(box_A, box_B).perform()
        # drop_place = actionChains.drag_and_drop_by_offset(box_A, 90, 290).perform()
        # time.sleep(2)
        print(drop_place)

        # I tried to drop box A to box B in different ways but I could not get any proper results :(

    def tearDown(self):
        self.driver.quit()