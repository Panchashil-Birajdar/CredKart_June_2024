import time

from pageObjects.Login_Page import Login_Class
from utilities.Logger import LoggingClass
from utilities  import XLUTILIES


class Test_Credkart_Login_DDT:
    log = LoggingClass.log_generator()
    path = ".\\Test_Data\\UserLogin.xlsx"

    # def test_credkart_url_DDT_001(self,setup):
    #     # self.log.debug("This is debug")
    #     # self.log.info("This is info")
    #     # self.log.warning("This is warning")
    #     # self.log.error("This is error")
    #     # self.log.critical("This is critical")
    #     self.log.info("Testcase test_credkart_url_DDT_001 is started")
    #     self.log.info("Opening browser")
    #     self.driver = setup
    #     if  self.driver.title=='CredKart':
    #         self.log.info("Taking Screenshot")
    #         self.driver.save_screenshot(".\\screenshots\\test_credkart_url_DDT_001.PNG")
    #         self.log.info("Testcase test_credkart_url_DDT_001 is passed")
    #         assert True
    #     else:
    #         self.log.info("Taking Screenshot")
    #         self.driver.save_screenshot(".\\screenshots\\test_credkart_url_DDT_002.PNG")
    #         self.log.info("Testcase test_credkart_url_DDT_001 is failed")
    #         assert False
    #     self.log.info("Testcase test_credkart_url_DDT_001 is completed")
    #     self.driver.close()

    def test_user_login_DDT_002(self,setup):
        self.log.info("Testcase test_user_login_DDT_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lg = Login_Class(self.driver)
        self.log.info("Opening login link")
        self.lg.Login_Link()
        self.rows = XLUTILIES.row_count(self.path,'Sheet1')

        Resul_List=[]
        for r in range(2,self.rows+1):
            print("no of rows in Excel file = " + str(r))
            self.Email = XLUTILIES.read_data(self.path,'Sheet1',r,1)
            self.Password = XLUTILIES.read_data(self.path,'Sheet1',r,2)
            self.Expected_Result = XLUTILIES.read_data(self.path,'Sheet1',r,3)


            self.log.info("Entering email" + self.Email)
            self.lg.Enter_Email(self.Email)
            self.log.info("Entering password" + self.Password)
            self.lg.Enter_Password(self.Password)
            self.log.info("Clicking on login button")
            self.lg.Click_Login_Button()
            if  self.Expected_Result == 'Login_Pass' and self.lg.Verify_Login()=='pass':
                self.driver.save_screenshot(".\\screenshots\\test_user_login_DDT_002_Pass.PNG")
                self.log.info("Testcase test_user_login_DDT_002 is passed")
                XLUTILIES.read_write(self.path,'Sheet1',r,4,'Login_Pass')
                Resul_List.append('Pass')
                time.sleep(2)
                self.lg.Click_Menu_Button()
                time.sleep(2)
                self.lg.Click_Logout_Button()
                self.lg.Login_Link()
            elif self.Expected_Result == 'Login_Pass' and self.lg.Verify_Login()=='fail':
                self.driver.save_screenshot(".\\screenshots\\test_user_login_DDT_002_Pass.PNG")
                self.log.info("Testcase test_user_login_DDT_002 is passed")
                XLUTILIES.read_write(self.path,'Sheet1',r,4,'Login_Fail')
                Resul_List.append('Fail')
                time.sleep(2)
                self.lg.Login_Link()
                time.sleep(2)
            elif self.Expected_Result == 'Login_Fail' and self.lg.Verify_Login()=='pass':
                self.driver.save_screenshot(".\\screenshots\\test_user_login_DDT_002_Pass.PNG")
                self.log.info("Testcase test_user_login_DDT_002 is passed")
                XLUTILIES.read_write(self.path,'Sheet1',r,4,'Login_Fail')
                Resul_List.append('Fail')
                time.sleep(2)
                self.lg.Login_Link()
                time.sleep(2)
            elif self.Expected_Result == 'Login_Fail' and self.lg.Verify_Login()=='fail':
                self.driver.save_screenshot(".\\screenshots\\test_user_login_DDT_002_Pass.PNG")
                self.log.info("Testcase test_user_login_DDT_002 is passed")
                XLUTILIES.read_write(self.path, 'Sheet1', r, 4, 'Login_Fail')
                Resul_List.append('Pass')

        print(Resul_List)
        if  'Fail' in Resul_List:
            self.log.info("Testcase test_user_login_DDT_002 is failed")
            assert False
        else:
            self.log.info("Testcase test_user_login_DDT_002 is Passed")
            assert True






































































































































































































































































