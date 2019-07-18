from selenium import webdriver
import pytest
import allure
from pages.loginPage import LoginPage
from pages.homepage import HomePage
from utils import utils as utils
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:

            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "OrangeHRM"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime =  moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = utils.whoami()
            screenshotName =  testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Rameesha/PycharmProjects/AutomationFrameworkPractice_1/screenshots/" + screenshotName + ".png")
            raise

        except:
            print("Exception")
            currTime = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            raise
        else:
            print("No exception")
        finally:
            print("Finally block")

