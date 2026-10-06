import pytest
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def setup():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(r'https://canvazo.com/')
    yield driver
    driver.close()
@pytest.fixture
def wait(setup):
    return WebDriverWait(setup, 10)