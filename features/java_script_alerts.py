import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time


class JavaScriptAlerts(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.alerts_url = self.base_url + 'javascript_alerts'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_alert_one(self):
        firts_alert_btn_path = '//*[@id="content"]/div/ul/li[1]/button'
        alert_results_path = '//*[@id="result"]'
        expected_text_in_alert = 'You successfully clicked an alert'
        driver = self.driver
        driver.get(self.alerts_url)

        btn_alert = driver.find_element_by_xpath(firts_alert_btn_path).click()
        alert = Alert(driver)
        print("Alert shows following message: " + alert.text)
        alert.accept()
        message = driver.find_element_by_xpath(alert_results_path).text
        self.assertEqual(expected_text_in_alert, message,
                         f'Message should say: {message}')
        print(message)

    def test_alert_two(self):
        second_alert_btn_path = '//*[@id="content"]/div/ul/li[2]/button'
        alert_results_path = '//*[@id="result"]'
        expected_text_in_alert = 'You clicked: Ok'
        driver = self.driver
        driver.get(self.alerts_url)

        btn_alert = driver.find_element_by_xpath(second_alert_btn_path).click()
        alert = Alert(driver)
        print("Alert shows following message: " + alert.text)
        alert.accept()
        message = driver.find_element_by_xpath(alert_results_path).text
        self.assertEqual(expected_text_in_alert, message,
                         f'Message should say: {message}')
        print(message)

    def test_alert_three(self):
        third_alert_btn_path = '//*[@id="content"]/div/ul/li[3]/button'
        alert_results_path = '//*[@id="result"]'
        expected_text_in_alert = 'You entered: How is my spaghetti code looks like?'
        driver = self.driver
        driver.get(self.alerts_url)

        btn_alert = driver.find_element_by_xpath(third_alert_btn_path).click()
        alert = Alert(driver)
        print("Alert shows following message: " + alert.text)
        alert.send_keys('How is my spaghetti code looks like?')
        alert.accept()
        message = driver.find_element_by_xpath(alert_results_path).text
        self.assertEqual(expected_text_in_alert, message,
                         f'Message should say: {message}')
        print(message)

    def tearDown(self):
        self.driver.quit()