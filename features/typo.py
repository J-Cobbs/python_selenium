import unittest
from selenium import webdriver

class Typo(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://the-internet.herokuapp.com/'
        self.typo_url = self.base_url + 'typos'
        self.driver = webdriver.Chrome(executable_path=r'/Applications/TestFiles/chromedriver')

    def test_typo_first_paragraph(self):
        first_paragraph_path = '//*[@id="content"]/div/p[1]'
        # first_paragraph_expected_text = "This example demonstrates a typo being introduced. It does it randomly on each page load."
        driver = self.driver
        driver.get(self.typo_url)

        first_parapraph = self.driver.find_element_by_xpath(first_paragraph_path).text
        # self.assertEqual(first_parapraph, first_paragraph_expected_text,
        #                  f'Houston, we have a typo here! In first paragraph')
        if first_parapraph == "This example demonstrates a typo being introduced. It does it randomly on each page load.":
            print('No typos in first paragraph')
        else:
            print(f'Houston, we have a typo here! In the first paragraph: {first_parapraph}')


    def test_typo_second_paragraph(self):
        second_paragraph_path = '//*[@id="content"]/div/p[2]'
        # second_paragraph_expected_text = "Sometimes you'll see a typo, other times you won't."
        driver = self.driver
        driver.get(self.typo_url)

        second_paragraph = driver.find_element_by_xpath(second_paragraph_path).text
        # self.assertEqual(second_paragraph, second_paragraph_expected_text,
        #                  f'Houston, we have a typo here! In second paragraph')
        if second_paragraph == "Sometimes you'll see a typo, other times you won't.":
            print('No typos in second paragraph')
        else:
            print(f'Houston, we have a typo here! In the second paragraph: {second_paragraph}')


    def tearDown(self):
        self.driver.quit()

    """Both tests may be run twice or 3 times so You can see if indeed there is a typo.
    We can use assertion or If statement
    """