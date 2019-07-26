
class LoginPage():
    def __init__(self,driver):
        self.driver=driver
        self.username_inputbox='[name="UserName"]'
        self.pwd_inputbox='[name="Password"]'
        self.login_button='[type="submit"]'


    def enter_username(self,uname):
        self.driver.find_element_by_css_selector(self.username_inputbox).clear()
        self.driver.find_element_by_css_selector(self.username_inputbox).send_keys(uname)

    def enter_pwd(self,pwd):
        self.driver.find_element_by_css_selector(self.pwd_inputbox).clear()
        self.driver.find_element_by_css_selector(self.pwd_inputbox).send_keys(pwd)

    def click_login_btn(self):
        self.driver.find_element_by_css_selector(self.login_button).click


