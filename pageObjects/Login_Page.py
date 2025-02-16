from selenium.webdriver.common.by import By


class Login_Class:
    click_login_link_XPATH = (By.XPATH,"//a[normalize-space()='Login']")
    text_email_XPATH = (By.XPATH,"//input[@id='email']")
    text_password_XPATH = (By.XPATH,"//input[@id='password']")
    click_login_button_XPATH = (By.XPATH,"//button[@type='submit']")
    verify_login_XPATH =(By.XPATH,"//h2[normalize-space()='CredKart']")
    menu_button_XPATH = (By.XPATH,"//a[@role='button']")
    logout_button_XPATH = (By.XPATH,"//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver = driver

    def Login_Link(self):
        self.driver.find_element(*Login_Class.click_login_link_XPATH).click()

    def Enter_Email(self,email):
        self.driver.find_element(*Login_Class.text_email_XPATH).send_keys(email)

    def Enter_Password(self,password):
        self.driver.find_element(*Login_Class.text_password_XPATH).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(*Login_Class.click_login_button_XPATH).click()

    def Click_Menu_Button(self):
        self.driver.find_element(*Login_Class.menu_button_XPATH).click()

    def Click_Logout_Button(self):
        self.driver.find_element(*Login_Class.logout_button_XPATH).click()

    def Verify_Login(self):
        try:
            self.driver.find_element(*Login_Class.verify_login_XPATH)
            return "pass"
        except:
            return "fail"








































































































































































































































































