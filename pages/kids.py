from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
import time

class KidsPage(BasePage):
    kid_actions=("xpath","(//a[@class='nav-link dropdown-menu-item'])[8]")
    drawing_coloring_link=("xpath","//a[text()='Drawing and Colouring']")
    product1=("xpath","(//a[@title='Anupam Sketcho Sketchbook - 140 GSM Cartridge Paper - Wire-O Binding'])")
    add_to_cart1=("xpath","(//button[@type='submit'])[3]")
    # quantity6=("xpath","//label[@for='option-1-1']")
    kids_colour_painting=("xpath","//a[@href='/collections/kids-paints-and-colours']")
    drawing_book=("xpath","(//a[@href='/collections/drawing-books'])[1]")
    poster_colour=("xpath","(//a[@href='/collections/poster-colours'])[1]")
    tempera_colour=("xpath","(//a[@href='/collections/tempera-colours'])[1]")
    gift_set=("xpath","(//a[@href='/collections/diy-kits-1'])[1]")
    crayons=("xpath","(//a[@href='/collections/crayons'])[1]")
    colour_pencil=("xpath","(//a[@href='/collections/colour-pencils'])[1]")
    sketch_pens=("xpath","(//a[@href='/collections/sketch-pens'])[1]")

    def __init__(self,driver):
        super().__init__(driver)

    def go_to_kids(self):
        self.hover(self.kid_actions)
        time.sleep(5)
    def go_to_drawing_coloring(self):
        self.hover(self.drawing_coloring_link)
        self.click(self.drawing_coloring_link)
        self.click(self.product1)
        self.click(self.add_to_cart1)
        # self.click(self.quantity6)







