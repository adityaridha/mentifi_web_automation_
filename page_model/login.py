from page_model import BasePage
from selenium.webdriver.common.by import By

class Login(BasePage):

    loc_email = (By.ID, "Email")
    loc_password = (By.ID, "Password")
    loc_login_button = (By.XPATH, "//button[@class='btn btn-azure btn-lg btn-block']")
    loc_forgot_password = (By.XPATH, "//a[contains(text(),'Forgot your password')]")

    def __init__(self):
        super().__init__()

    def verify_login_page_elements(self):
        login_element = [self.loc_email, self.loc_password, self.loc_login_button, self.loc_forgot_password]
        self.verify_elements(elements=login_element)

    def input_email_address(self, email):
        print("\n[LOGIN PAGE] input email data : {}".format(email))
        self.find_element(self.loc_email).send_keys(email)

    def input_password(self, password):
        print("[LOGIN PAGE] input password data : {}".format(password))

        self.find_element(self.loc_password).send_keys(password)

    def click_login_button(self):
        print("[LOGIN PAGE] click login button")
        self.find_element(self.loc_login_button).click()

    def click_forgot_password(self):
        print("[LOGIN PAGE] click forgot password button")
        self.find_element(self.loc_forgot_password).click()

    def login_as_mentor(self, name, password):
        self.verify_login_page_elements()
        self.input_email_address(name)
        self.input_password(password)
        self.click_login_button()

    def login_as_mentee(self, name, password):
        self.verify_login_page_elements()
        self.input_email_address(name)
        self.input_password(password)
        self.click_login_button()


