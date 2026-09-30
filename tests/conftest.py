import pytest

@pytest.fixture()
def setup():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get(r'https://www.jiosaavn.com/')
    yield driver
    driver.close()