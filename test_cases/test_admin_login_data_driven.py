import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import LoginAdminPage
from test_cases.conftest import setup
from utilities.read_properties import  ReadConfig
from utilities.custom_logger import LogMaker
from utilities import excel_utils
class Test02AdminLoginDataDriven:

    ##use Read config class to read common static method data
    admin_page_url = ReadConfig.get_admin_page_url()
    path = ".//test_data/admin_login_data.xlsx"

    # store status
    status_list =[]

    ## call logmaker class to get logger object
    logger = LogMaker.log_gen()



    def test_valid_admin_login_data_driven(self,setup):

        self.logger.info("******data driven Testing************")

        ##create driver instance
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.implicitly_wait(10)

        ##create object of admin page
        self.admin_login = LoginAdminPage(self.driver)

        ##pass data from excel sheet
        self.rows = excel_utils.getRowCount(self.path,"Data")
        print("no of rows",self.rows)

        ##iterate all the data using for loop
        for r in range(2,self.rows+1):
            self.username = excel_utils.readCellData(self.path,"Data",r,1)
            self.password = excel_utils.readCellData(self.path,"Data",r,2)
            self.exp_login = excel_utils.readCellData(self.path,"Data",r,3)

            self.admin_login.enter_username(self.username)
            self.admin_login.enter_password(self.password)
            self.admin_login.click_login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data passed")
                    self.status_list.append("Pass")
                    self.admin_login.click_logout()
                elif self.exp_login == "No":
                    self.logger.info("test data failed")
                    self.status_list.append("Fail")
                    self.admin_login.click_logout()
            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data failed")
                    self.status_list.append("Fail")
                elif self.exp_login == "No":
                    self.logger.info("test data passed")
                    self.status_list.append("Pass")

        print("status list is ", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test data driven admin login is failed")
            assert False
        else:
            self.logger.info("Test data driven admin login is Passed")
            assert True



