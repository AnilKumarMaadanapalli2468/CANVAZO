from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.kid_base_page import BasePage
import time

class Stationery(BasePage):
     stationery= ('xpath','(//a[@class="nav-link dropdown-menu-item"])[5]')
     Desk=('xpath','//a[@class="menu-category-title" and normalize-space()="Desk Accessories"]')
     Brand = ('xpath',"//label[@for='Filter-brand-5']")
     Selectitem = (By.CSS_SELECTOR,
        "div[data-product-grid] a.yv-product-img")
     Button=(By.CSS_SELECTOR,'button[class="Sd_addProduct add_to_cart button med-btn"]')
     CloseButton=(By.CSS_SELECTOR,'button[class="yv_side_drawer_close"]')
     DrinkWaterbottle = (
         By.XPATH,
         "//div[contains(@class,'dropdown-inner-menu-item')][.//a[normalize-space()='Desk Accessories']]//a[normalize-space()='Drinkware & Water Bottles']"
     )

     # DrinkWaterbottle = ("xpath", "//a[text()='Drinkware & Water Bottles']")
     Sharpners=( By.XPATH,
         "//div[contains(@class,'dropdown-inner-menu-item')]"
         "[.//a[normalize-space()='Desk Accessories']]"
         "//a[normalize-space()='Sharpners & Erasers']")
     Handcrafted = (
         By.XPATH,
         "//a[@href='/collections/handcrafted-diaries' and normalize-space()='Handcrafted Diaries']"
     )



     Pens=("xapth","//a[text()='Pens and Pencils']")

     Adhesives = ('xpath', '//a[@class="menu-category-title" and normalize-space()="Adhesives"]')
     Instock=(By.XPATH,
        "//*[contains(normalize-space(), 'In stock')]")
     Journal = ('xpath', '//a[@class="menu-category-title" and normalize-space()="Journal and Notebooks"]')
         # ("id","Filter - availability - 1")
     def __init__(self, driver):
         super().__init__(driver)
         self.wait = WebDriverWait(driver, 10)

     def click_stationery(self):
         stationery_element = self.wait.until(
             EC.visibility_of_element_located(self.stationery)
         )

         ActionChains(self.driver).move_to_element(
             stationery_element
         ).perform()



     def click_desk(self):
        self.click(self.Desk)
        time.sleep(2)
     def click_brand(self):
         self.click(self.Brand)
     def click_item(self):
         self.click(self.Selectitem)
     def click_button(self):
         self.click(self.Button)
     def click_closebutton(self):
         self.click(self.CloseButton)

     def click_drinkwater(self):
         # Go back to home page
         self.driver.get("https://canvazo.com/")

         # Wait for Stationery
         stationery_element = self.wait.until(
             EC.visibility_of_element_located(self.stationery)
         )

         # Open Stationery menu
         ActionChains(self.driver).move_to_element(
             stationery_element
         ).perform()

         time.sleep(2)

         # Find the complete Desk Accessories menu section
         desk_menu = self.wait.until(
             EC.visibility_of_element_located(self.Desk)
         )

         # Hover over the complete menu section
         ActionChains(self.driver).move_to_element(
             desk_menu
         ).perform()

         time.sleep(2)

         # Find Drinkware
         drink_element = self.wait.until(
             EC.visibility_of_element_located(
                 self.DrinkWaterbottle
             )
         )

         # Click Drinkware
         ActionChains(self.driver).move_to_element(
             drink_element
         ).click().perform()
     def click_sharpner(self):
         self.click(self.Sharpners)
     def click_pen(self):
         self.click_button()
     def scroll_up(self):
         self.driver.execute_script("window.scrollTo(0, 0);")
     def click_adhesive(self):
         self.click(self.Adhesives)
     def click_instock(self):
         self.click(self.Instock)
     def click_journal(self):
         self.click(self.Journal)

     def click_handcrafted(self):
         # Scroll to top
         self.driver.execute_script("window.scrollTo(0, 0);")

         # Open Stationery menu
         stationery_element = self.wait.until(
             EC.visibility_of_element_located(self.stationery)
         )

         ActionChains(self.driver).move_to_element(
             stationery_element
         ).perform()

         time.sleep(2)

         # Find Handcrafted Diaries in the DOM
         handcrafted_element = self.wait.until(
             EC.presence_of_element_located(self.Handcrafted)
         )

         # Scroll to the element
         self.driver.execute_script(
             "arguments[0].scrollIntoView({block: 'center'});",
             handcrafted_element
         )

         time.sleep(1)

         # Click using JavaScript
         self.driver.execute_script(
             "arguments[0].click();",
             handcrafted_element
         )