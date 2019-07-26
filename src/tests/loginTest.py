import unittest
from selenium import webdriver
import time
from src.pages.loginPage import LoginPage
import HtmlTestRunner


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            "/Users/rajkumarsethi/PycharmProjects/SeleniumProject/resources/drivers/chromedriver")
        cls.driver.get("http://executeautomation.com/demosite/Login.html")
        time.sleep(3)

    def test_verify_login(self):
        login = LoginPage(self.driver)
        login.enter_username("raj.sethi")
        login.enter_pwd("hello")
        login.click_login_btn()
        # assert self.driver.find_element_by_tag_name("h1").text == "Execute Automation Selenium Test Site"
        self.assertEquals(self.driver.find_element_by_tag_name("h1").text, "Execute Automation Selenium Test Site",
                          "failed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/rajkumarsethi/PycharmProjects/SeleniumProject/results"))
