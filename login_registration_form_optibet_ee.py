import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class LoginRegistartionForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_registerForm(self):
        driver = self.driver
        driver.get("https://www.optibet.ee")
        time.sleep(3)
        registerbutton = driver.find_element_by_link_text("REGISTREERU").click()
        time.sleep(2)
        name_input = driver.find_element_by_id("firstname").send_keys('Inga')
        surname_input = driver.find_element_by_id("lastname").send_keys('Lember')
        email_input = driver.find_element_by_id("email").send_keys('inst94@icloud.com')
        phone_input = driver.find_element_by_id("phone").send_keys('56633937')
        personalcode_input = driver.find_element_by_id("personalcode").send_keys('49404010867')
        gender_select = driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div/div[2]/div/div/div/div/div/div[1]/form/ul/li[5]/div[2]/div/div[3]/label[2]/span').click()
        adress_input = driver.find_element_by_id("address").send_keys('Akadeemia tee 68-54')
        city_input = driver.find_element_by_id("city").send_keys('Tallinn')
        index_input = driver.find_element_by_id("post").send_keys('12614')
        useraname_input = driver.find_element_by_id("username").send_keys('inst94')
        password_input = driver.find_element_by_id("password").send_keys('abc1234')
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div/div[2]/div/div/div/div/div/div[1]/form/ul/li[8]/div[1]/div/div[2]/div/div/button/span[2]').click()
        time.sleep(3)
        question_select = driver.find_element_by_link_text('Mis tänaval sa üles kasvasid?').click()
        answer_input = driver.find_element_by_id("secret-answer").send_keys('Akadeemia')
        rules = driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div/div[2]/div/div/div/div/div/div[1]/form/ul/li[11]/label/span').click()
        craete_account = driver.find_element_by_id("submit").click()
        time.sleep(3)
    def test_login(self):
        driver = self.driver
        driver.get("https://www.optibet.ee")
        username = driver.find_element_by_css_selector("#dummy_username")
        username.click()
        username.send_keys('inst94')

        password = driver.find_element_by_css_selector("#dummy_passwd")
        password.click()
        password.send_keys('abc1234')

        login = driver.find_element_by_css_selector("#form-login > input.sign-in-panel__submit.button")
        login.click()

        time.sleep(3)
    def testClose(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
