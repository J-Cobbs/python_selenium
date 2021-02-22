from helpers.base_test_class import BaseTestClass
from helpers import login_helper as lh

class HerokuappLoginPageTests(BaseTestClass):
    def test_incorrect_login(self):
        # This test will fail due to double line
        expected_text = 'Login Page'
        header_xpath = '//*[@id="content"]/div/h2'
        user_email = 'invalid@test.test'
        user_pass = 'abc123'
        login_button = '//*[@id="login"]/button'
        driver = self.driver

        driver.get(self.login_url)
        lh.user_login(driver, user_email, user_pass)
        self.driver.find_element_by_xpath(login_button).click()
        self.assert_element_text(driver, header_xpath, expected_text)

    def test_correct_login(self):
        expected_text = 'Welcome to the Secure Area. When you are done click logout below.'
        alert_xpath = '//*[@id="content"]/div/h4'
        user_email = 'tomsmith'
        user_pass = 'SuperSecretPassword!'
        login_button = '//*[@id="login"]/button'
        driver = self.driver

        driver.get(self.login_url)
        lh.user_login(driver, user_email, user_pass)
        self.driver.find_element_by_xpath(login_button).click()
        self.assert_element_text(driver, alert_xpath, expected_text)

    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

         :param driver: webdriver instance
         :param xpath: xpath to element with text to be observed
         :param expected_text: text what we expecting to be found
         :return: None
        """
        element = driver.find_element_by_xpath(xpath)
        element_text = element.text
        self.assertEqual(expected_text, element_text, f'Expected text differ from actual on page: {driver.current_url}')