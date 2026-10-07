from pages.BrushesAndAccessories import  BRUSHES_AND_ACCESSORIES

def test_B_and_A(setup):
    driver = setup
    BA=BRUSHES_AND_ACCESSORIES(driver)
    BA.click_B_and_A()
    BA.click_brushes()
    BA.check_stock()
    BA.move_price_slider()



