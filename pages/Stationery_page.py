from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.kid_base_page import BasePage
import time

class Stationery(BasePage):
     stationery= ('xpath','(//a[@class="nav-link dropdown-menu-item"])[5]')
     Selectitem = (By.CSS_SELECTOR,
        "div[data-product-grid] a.yv-product-img")
     Button=(By.CSS_SELECTOR,'button[class="Sd_addProduct add_to_cart button med-btn"]')
     CloseButton=(By.CSS_SELECTOR,'button[class="yv_side_drawer_close"]')
     Instock = (
         By.CSS_SELECTOR,
         "label[for='Filter-availability-1']"
     )
     Clearall=('id',"yv-applied-filter-cross-all")

     def __init__(self, driver):
         super().__init__(driver)
         self.wait = WebDriverWait(driver, 10)
     #  start of new code
     def category_locator(self,category_name):
         return(
             By.XPATH,f"//a[contains(@class,'menu-category-title') "
             f"and normalize-space()='{category_name}']")

     def submenu_locator(self, category_name, item_name):
         return (
             By.XPATH,
             f"//div[contains(@class,'dropdown-inner-menu-item')]"
             f"[.//a[contains(@class,'menu-category-title') "
             f"and normalize-space()='{category_name}']]"
             f"//a[normalize-space()='{item_name}']"
         )

     def click_stationery_submenu(self, category_name, item_name):
         # Hover Stationery
         self.hover(self.stationery)

         # Hover parent category
         self.hover(
             self.category_locator(category_name)
         )

         # Find child item
         child = self.wait.until(
             EC.element_to_be_clickable(
                 self.submenu_locator(
                     category_name,
                     item_name
                 )
             )
         )

         # Click child
         child.click()

     #     my code
     def click_stationery_menu(self, category_name):
         # Hover Stationery
         self.hover(self.stationery)

         # Hover parent category
         self.hover(
             self.category_locator(category_name)
         )

         # Find child item
         parent = self.wait.until(
             EC.element_to_be_clickable(
                 self.category_locator(
                     category_name
                 )
             )
         )

         # Click child
         parent.click()
     # end of new code
     def click_item(self):
         self.click(self.Selectitem)
     def click_button(self):
         self.click(self.Button)
     def click_closebutton(self):
         self.click(self.CloseButton)

     def scroll_up(self):
         self.driver.execute_script("window.scrollTo(0, 0);")

     def click_instock(self):
         self.click(self.Instock)
     def click_clearall(self):
         self.click(self.Clearall)
