import pytest
import allure
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome=yield
    report=outcome.get_result()
    if report.when=="call" and report.failed:
        driver=item.funcargs.get("setup")
        if driver:
            allure.attach(driver.get_screenshot_as_png(),
                          name="failure screenshot",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(
                driver.current_url,
                name="Current URL",
                attachment_type=allure.attachment_type.TEXT)
            allure.attach(
                driver.page_source,
                name="Page Source",
                attachment_type=allure.attachment_type.HTML)
            allure.attach.file(
                "logs/application.log",
                name="Application Log"
            )