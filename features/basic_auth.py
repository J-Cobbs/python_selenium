import unittest
import time
from selenium import webdriver

class BasicAuth(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.login_url = self.base_url + 'basic_auth'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_correct_basic_auth(self):
        driver = self.driver
        driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')
        time.sleep(2)
        #element = driver.find_element_by_xpath("//*[@id='content']/div/p")
        #element = element.text
        element = driver.find_element_by_xpath("//*[@id='content']/div/p").text
        print(element)
        element_text = 'Congratulations! You must have the proper credentials.'
        self.assertEqual(element, element_text, f'Text is as expected')

    def tearDown(self):
        self.driver.quit()