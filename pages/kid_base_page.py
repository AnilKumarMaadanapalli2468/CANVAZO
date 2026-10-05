from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium .webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions=ActionChains(driver)

    def hover(self,locator):
        element=self.wait.until(EC.visibility_of_element_located(locator))
        self.actions.move_to_element(element).perform()

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text