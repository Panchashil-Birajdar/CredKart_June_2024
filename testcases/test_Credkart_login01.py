from pageObjects.Login_Page import Login_Class
from utilities.Logger import LoggingClass
from utilities.readConfigFile import ReadConfigClass


class Test_Credkart_Login:
    log = LoggingClass.log_generator()
    Email = ReadConfigClass.getEmail()
    Password = ReadConfigClass.getPassword()

    def test_credkart_url_001(self,setup):
        # self.log.debug("This is debug")
        # self.log.info("This is info")
        # self.log.warning("This is warning")
        # self.log.error("This is error")
        # self.log.critical("This is critical")
        self.log.info("Testcase test_credkart_url_001 is started")
        self.log.info("Opening browser")
        self.driver = setup
        if  self.driver.title=='CredKart':
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\screenshots\\test_credkart_url_001.PNG")
            self.log.info("Testcase test_credkart_url_001 is passed")
            assert True
        else:
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\screenshots\\test_credkart_url_002.PNG")
            self.log.info("Testcase test_credkart_url_001 is failed")
            assert False
        self.log.info("Testcase test_credkart_url_001 is completed")
        self.driver.close()

    def test_user_login_002(self,setup):
        self.log.info("Testcase test_user_login_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lg = Login_Class(self.driver)
        self.log.info("Opening login link")
        self.lg.Login_Link()
        self.log.info("Entering email")
        self.lg.Enter_Email(self.Email)
        self.log.info("Entering password")
        self.lg.Enter_Password(self.Password)
        self.log.info("Clicking on login button")
        self.lg.Click_Login_Button()
        if  self.lg.Verify_Login()=='pass':
            self.log.info("Testcase test_user_login_002 is passed")
            self.driver.save_screenshot(".\\screenshots\\test_user_login_002_Pass.PNG")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_user_login_002_Fail.PNG")
            self.log.info("Testcase test_user_login_002 is failed")
            assert False
        self.driver.close()





































































































































































































































































