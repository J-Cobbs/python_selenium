import unittest
from selenium import webdriver

class Redirect(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.redirect_url = self.base_url + 'redirector'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_redirect(self):
        driver = self.driver
        driver.get(self.redirect_url)
        redicrect_btn_path = '//*[@id="redirect"]'
        status_code_header_path = '//*[@id="content"]/div/h3'
        paragraph_status_path = '//*[@id="content"]/div/p'
        paragraph_expected_text_path = 'This page returned a 500 status code.\n\nFor a definition and common list of HTTP status codes, go here'
        status_200_path = '//*[@id="content"]/div/ul/li[1]/a'
        status_500_path = '//*[@id="content"]/div/ul/li[4]/a'
        back_to_status_code_path = '//*[@id="content"]/div/p/a'

        print(driver.current_url)
        redirect_btn = driver.find_element_by_xpath(redicrect_btn_path).click()
        header = driver.find_element_by_xpath(status_code_header_path).text
        print('Current page is ' + header)
        status_200_btn = driver.find_element_by_xpath(status_200_path).click()
        paragraph = driver.find_element_by_xpath(paragraph_status_path).text
        print(paragraph)
        back_btn = driver.find_element_by_xpath(back_to_status_code_path).click()
        status_500_btn = driver.find_element_by_xpath(status_500_path).click()
        paragraph = driver.find_element_by_xpath(paragraph_status_path).text
        print(paragraph)
        self.assertRegex(paragraph_expected_text_path, paragraph,
                         f'This is not a proper paragraph')

    def tearDown(self):
        self.driver.quit()