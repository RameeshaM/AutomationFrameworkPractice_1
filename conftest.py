import pytest


def pytest_addoption(parser):
        parser.addoption("--browser", action="store", default="Chrome", help="Test the browser")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")

    if browser == "Chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/Rameesha/PycharmProjects/AutomationFrameworkPractice_1/drivers/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.close()
        driver.quit()
        print("Test")