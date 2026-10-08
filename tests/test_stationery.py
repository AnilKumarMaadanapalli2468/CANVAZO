from pages.Stationery_page import Stationery
import time
import allure
@allure.title('Verify the stationery')
@allure.description('verify the user to open the stationery report')
def test_stationery(setup):
    S = Stationery(setup)
    with allure.step("Desk accesories"):
         S.click_stationery_menu("Desk Accessories")
    with allure.step("click the item"):
         S.click_item()
    S.click_button()
    S.click_closebutton()
    S.scroll_up()
    S.click_stationery_submenu(
        "Desk Accessories",
        "Drinkware & Water Bottles"
    )
    S.click_stationery_submenu("Adhesives","Tapes")
    S.click_stationery_submenu("Journal and Notebooks", "Handcrafted Diaries")
    S.click_instock()
    time.sleep(3)
    S.click_clearall()
    time.sleep(2)
