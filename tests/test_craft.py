from pages.craft_page import CraftPage
def test_craft_foils(setup):
    driver = setup
    C=CraftPage(driver)
    C.click_craft_menu()
    C.click_foils()
    driver.quit()
