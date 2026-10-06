from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains,Keys
from pages.base_page import BasePage

class CART(BasePage):
    search = ('id',"search-drawer-query-input")
    # seacrh_button = ('css selector',"//*[name()='svg' and @id='Layer_2']")
    product = ('xpath',"//a[contains(text(),'Apolix Twisty Crayons 6 Colours ')]")
    forward = ('xpath','(//*[name()="svg" and @class="flickity-button-icon"])[2]')
    quantity_inc = ('xpath','(//button[@type="button"])[5]')
    add_to_cart = ('css selector','[class="Sd_addProduct add_to_cart button med-btn"]')
    quantity_dec = ('xpath','(//button[@type="button"])[9]')
    check_out = ('xpath','//a[@class="checkout-btn button black-btn"]')


    def click_search(self,enter):
        ele = self.wait.until(EC.element_to_be_clickable(self.search))
        ele.send_keys(enter)
        ele.send_keys(Keys.ENTER)

    def scroll_to_product(self):
        scrol = self.wait.until(EC.presence_of_element_located(self.product))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",scrol)
        self.wait.until(EC.element_to_be_clickable(self.product)).click()

    def clik_forward(self):
        self.click(self.forward)

    def inc_quant(self):
        quant = self.wait.until(EC.presence_of_element_located(self.quantity_inc))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",quant)
        self.wait.until(EC.element_to_be_clickable(self.quantity_inc)).click()

    def ca_rt(self):
        self.click(self.add_to_cart)

    def dec_quant(self):
        self.click(self.quantity_dec)

    def cliq_checkout(self):
        self.click(self.check_out)





