from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.Basepage import BasePage


class HomePage(BasePage):

    brand_option = (By.XPATH, '(//a[@href="/pages/brands"])[1]')
    brand_logo = (By.XPATH, '//a[@aria-label="Canvazo"]//img')
    brands = (By.XPATH, '(//div[@class="yv-dropdown-menus"])[9]//a')
    brand_name = (By.XPATH, "(//a[text()='Roy'])[2]")
    product_titles = (By.CSS_SELECTOR, '.yv-product-title')
    def __init__(self, driver):
        super().__init__(driver)

    def click_brand_option(self):
        self.click(self.brand_option)

    def verify_brand_logos(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.brand_logo)
        ).is_displayed()
    def click_brand_popup(self):
        self.hover(self.brand_option)
        self.click(self.brand_name)

    def verify_all_products_same_brand(self):
        selected_brand = self.driver.find_element(*self.brand_name).text.strip().lower()

        products = self.driver.find_elements(*self.product_titles)

        for product in products:
            product_name = product.text.lower()

            if selected_brand not in product_name:
                return False

        return True

    def print_all_brands(self):
        brands = self.driver.find_elements(*self.brands)

        for brand in brands:
            print(brand.text)

    def get_all_brands(self):
        brands = self.driver.find_elements(*self.brands)

        return [
            brand.text.strip()
            for brand in brands
            if brand.text.strip() and "-" not in brand.text
        ]

    def click_brand(self, brand_name):
        brand = (By.XPATH, f'(//a[text()="{brand_name}"])[2]')
        self.click(brand)

    def Verify_all_products_same_brand(self, brand_name):
        products = self.driver.find_elements(*self.product_titles)

        expected = (
            brand_name.lower()
            .replace("-", "")
            .replace("&", "and")
            .replace(" ", "")
        )

        for product in products:
            actual = (
                product.text.lower()
                .replace("-", "")
                .replace("&", "and")
                .replace(" ", "")
            )

            print("Expected:", expected)
            print("Actual:", actual)

            if expected not in actual:
                print("FAILED PRODUCT:", product.text)
                return False

        return True





