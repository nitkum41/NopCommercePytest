import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import LoginAdminPage
from test_cases.conftest import setup
from utilities.read_properties import  ReadConfig

class Test01AdminLogin:

    ##use Read config class to read common static method data
    admin_page_url = ReadConfig.get_admin_page_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()

    def test_title_verification(self, setup):
        self.driver = setup ## fixtures for repetiive code
        self.driver.get(self.admin_page_url)
        exp_title = "nopCommerce demo store. Logi"
        act_title = self.driver.title

        if act_title==exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png") ##add screenshots
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):

        ##create driver instance
        self.driver = setup
        self.driver.get(self.admin_page_url)

        ##create object of admin page
        self.admin_login = LoginAdminPage(self.driver)

        self.admin_login.enter_username(self.username)
        self.admin_login.enter_password(self.password)
        self.admin_login.click_login()

        act_dashboard_text = self.driver.find_element(By.XPATH,"// h1[normalize - space() = 'Dashboard']").text
        if act_dashboard_text == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False


    def test_invalid_admin_login(self,setup):

        ##create driver instance
        self.driver = setup
        self.driver.get(self.admin_page_url)

        ##create object of admin page
        self.admin_login = LoginAdminPage(self.driver)

        self.admin_login.enter_username(self.invalid_username)
        self.admin_login.enter_password(self.password)
        self.admin_login.click_login()

        error_message = self.driver.find_element(By.XPATH,"//li").text
        if error_message == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False
