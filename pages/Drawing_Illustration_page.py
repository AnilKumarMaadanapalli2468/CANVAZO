import time
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class DRAWING:
    drawing='(//a[@href="/collections/pen-pencils-and-markers"])[2]'
    in_stock='Filter-availability-1'
    min_price='Filter-Price-GTE'
    max_price='Filter-Price-LTE'
    categorie='Filter-categories-5'
    color='Filter-color-41'
    brand='Filter-brand-4'
    product='//img[@class="no-js-hidden product-second-img lazyautosizes ls-is-cached lazyloaded"]'
    next_img='(//*[name()="svg" and @class="flickity-button-icon"])[2]'
    quantity_inc = ('xpath', '(//button[@type="button"])[5]')
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    def click_drawings(self):
        self.driver.find_element('xpath',self.drawing).click()
        time.sleep(2)
    def click_in_stock(self):
        self.driver.find_element('id',self.in_stock).click()
        time.sleep(1)
    def pass_min_price(self,price_min):
        self.driver.find_element('id',self.min_price).send_keys(price_min)
        time.sleep(1)

    def pass_max_price(self, price_max):
        self.driver.find_element('id', self.max_price).send_keys(price_max)
        time.sleep(1)
    def click_categorie(self):
        self.driver.find_element('id',self.categorie).click()
        time.sleep(2)
    def click_color(self):
        self.driver.find_element('id',self.color).click()
        time.sleep(1)
    def click_brand(self):
        self.driver.find_element('id',self.brand).click()
        time.sleep(1)
    def click_on_product(self):
        self.driver.find_element('xpath',self.product).click()
        time.sleep(1)
    def click_next_img(self):
        self.driver.find_element('xpath',self.next_img).click()
        time.sleep(1)

    def inc_quant(self):
        quant = self.wait.until(EC.presence_of_element_located(self.quantity_inc))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", quant)
        self.wait.until(EC.element_to_be_clickable(self.quantity_inc)).click()
        time.sleep(1)