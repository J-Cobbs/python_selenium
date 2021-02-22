import unittest
from selenium import webdriver

class BaseTestClass(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.login_url = self.base_url + '/login'

        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def tearDown(self):
        self.driver.quit()