from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FoilsPage(BasePage):

    PRODUCT_LINK = (
        By.XPATH,
        "//a[contains(@href,'/products/')][1]")

    PRODUCT_NAME = (
        By.XPATH,
        "//a[contains(@href,'/products/')][1]"
    )

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def click_first_product(self):
        self.click(self.PRODUCT_LINK)