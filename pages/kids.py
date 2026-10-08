import allure
from selenium.webdriver.common.action_chains import ActionChains
from pages.kid_base_page import BasePage
import time

class KidsPage(BasePage):
    kid_actions=("xpath","(//a[@class='nav-link dropdown-menu-item'])[8]")
    drawing_coloring_link=("xpath","//a[text()='Drawing and Colouring']")
    product1=("xpath","(//a[@title='Anupam Sketcho Sketchbook - 140 GSM Cartridge Paper - Wire-O Binding'])")
    add_to_cart1=("xpath","(//button[@type='submit'])[3]")
    # quantity6=("xpath","//label[@for='option-1-1']")
    close=("xpath","//button[@class='yv_side_drawer_close']")
    kids_colour_painting=("xpath","//a[@href='/collections/kids-paints-and-colours']")
    sort1=("xpath","//button[@class='collection-sortby-selected']")
    price_high_to_low=("xpath","//input[@id='sortByOption-7']")
    products=("xpath","//a[@class='yv-product-title']")
    drawing_book=("xpath", "(//a[@href='/collections/drawing-books'])[2]")
    # from_lower=("xpath","//div[@class='noUi-handle noUi-handle-lower']")
    # from_higher=("xpath","//div[@class='noUi-handle noUi-handle-upper']")
    poster_colour=("xpath","(//a[@href='/collections/poster-colours'])[4]")
    from_lower = ("xpath", "//div[@class='noUi-handle noUi-handle-lower']")
    from_higher=("xpath","//div[@class='noUi-handle noUi-handle-upper']")
    tempera_colour=("xpath","(//a[@href='/collections/tempera-colours'])[4]")
    gift_set=("xpath","(//a[@href='/collections/diy-kits-1'])[2]")
    crayons=("xpath","(//a[@href='/collections/crayons'])[4]")
    colour_pencil=("xpath","(//a[@href='/collections/colour-pencils'])[4]")
    sketch_pens=("xpath","(//a[@href='/collections/sketch-pens'])[4]")

    def __init__(self,driver):
        super().__init__(driver)
    @allure.step("open kids category")
    def go_to_kids(self):
        self.hover(self.kid_actions)
        time.sleep(5)
    @allure.step("open drawing colouring")
    def go_to_drawing_coloring(self):
        self.hover(self.drawing_coloring_link)
        self.click(self.drawing_coloring_link)
        self.click(self.product1)
        self.click(self.add_to_cart1)
        self.click(self.close)
        time.sleep(3)
    @allure.step("open kids painting")
    def go_to_kids_painting(self):
        self.hover(self.kids_colour_painting)
        self.click(self.kids_colour_painting)
        self.click(self.sort1)
        self.click(self.price_high_to_low)
        self.click_last_available_product(self.products)
        time.sleep(3)
    def go_to_drawing_book(self):
         self.hover(self.drawing_book)
         self.click(self.drawing_book)
        # self.move_slider(self.from_lower)
        # self.move_slider(self.from_higher)
    @allure.step("open poster colouring")
    def go_to_poster_colour(self):
        self.hover(self.poster_colour)
        self.click(self.poster_colour)
        self.move_slider(self.from_lower,100)
        self.move_slider(self.from_higher,50)
    @allure.step("open tempera colouring")
    def go_to_tempera_colour(self):
        self.hover(self.tempera_colour)
        self.click(self.tempera_colour)
    @allure.step("open gift set")
    def go_to_gift_set(self):
        self.hover(self.gift_set)
        self.click(self.gift_set)
    @allure.step("open crayons")
    def go_to_crayons(self):
        self.hover(self.crayons)
        self.click(self.crayons)
    @allure.step("open colour pencil")
    def go_to_colour_pencil(self):
        self.hover(self.colour_pencil)
        self.click(self.colour_pencil)
    @allure.step("open sketch pens")
    def go_to_sketch_pens(self):
        self.hover(self.sketch_pens)
        self.click(self.sketch_pens)













