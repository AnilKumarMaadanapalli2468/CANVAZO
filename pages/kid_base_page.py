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


    # def clicks(self, locator):
    #     products = self.wait.until(EC.presence_of_all_elements_located(locator))
    #
    #     for product in products:
    #         self.driver.execute_script("arguments[0].style.border='3px solid red';", product)
    #     products = self.wait.until(EC.presence_of_all_elements_located(locator))
    #     last_product = products[-1]
    #     self.wait.until(EC.visibility_of(last_product))
    #     self.actions.move_to_element(last_product).click().perform()

    def move_slider(self, locator, offset):
        handle = self.wait.until(EC.visibility_of_element_located(locator))

        self.actions.move_to_element(handle) \
            .click_and_hold() \
            .move_by_offset(offset, 0) \
            .release() \
            .perform()

    def click_last_available_product(self, locator):
        products = self.wait.until(EC.visibility_of_all_elements_located(locator))

        for product in reversed(products):

            print("Checking:", product.text)

            if "Out of Stock" not in product.text:
                self.driver.execute_script("arguments[0].style.border='3px solid red';",product)

                self.actions.move_to_element(product).click().perform()
                return

        raise Exception("No available product found")