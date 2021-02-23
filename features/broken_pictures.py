import unittest
from selenium import webdriver
import time

class BrokenImage(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.images_url = self.base_url + 'broken_images'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_pictures_check(self):
        broken_image = '//*[@id="content"]/div/img[1]'
        solid_image = '//*[@id="content"]/div/img[3]'
        driver = self.driver

        driver.get(self.images_url)
        # time.sleep(1)
        image_broken = driver.find_element_by_xpath(broken_image).get_property('src')
        print('This is a property of broken image ' + image_broken)
        image_solid = driver.find_element_by_xpath(solid_image).get_property('src')
        print('This is a property of solid image ' + image_solid)

    def tearDown(self):
        self.driver.quit()