from selenium import webdriver
import pytest
from model.applic import Application
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *


@pytest.fixture
def app(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 30)
    request.addfinalizer(driver.quit)
    return Application(driver,wait)