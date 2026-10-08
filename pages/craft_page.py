from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class CraftPage(BasePage):
    CRAFT_MENU = (By.XPATH, "//a[text()='Craft']")
    FOILS_OPTION = (By.XPATH,"//h1[@class='collection-banner-title']")
    def click_craft_menu(self):
        self.click(self.CRAFT_MENU)
    def click_foils(self):
        self.click(self.FOILS_OPTION)
