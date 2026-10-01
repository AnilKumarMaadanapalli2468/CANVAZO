from pages.cart_page import CART

def test_cart(setup):
    driver = setup
    C = CART(driver)
    C.click_search('crayons')
    C.scroll_to_product()
    C.clik_forward()
    C.inc_quant()
    C.ca_rt()
    C.dec_quant()
    C.cliq_checkout()