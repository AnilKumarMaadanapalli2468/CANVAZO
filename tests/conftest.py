import pytest

@pytest.fixture()
def setup():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get(r'https://canvazo.com/')
    yield driver
    driver.close()