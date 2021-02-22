def user_login(driver, user_email, user_pass):
   """
   Login user to website using given email and password

   :param driver: webdriver instance
   :param user_email: user email
   :param user_pass: user password
   :return: None
   """

   # finding login input box and sending value
   login_input_element = driver.find_element_by_xpath('//*[@id="username"]')
   login_input_element.send_keys(user_email)

   # finding password input box and sending value
   login_input_element = driver.find_element_by_xpath('//*[@id="password"]')
   login_input_element.send_keys(user_pass)

   # finding button 'SIGN IN'
   # button_next_element = driver.find_element_by_xpath('//*[@id="login"]/button')
   # button_next_element.click()