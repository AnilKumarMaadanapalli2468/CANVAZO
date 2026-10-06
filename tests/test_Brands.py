from selenium.webdriver.common.by import By

from pages.HomePage import HomePage


def test_brands_logo(setup):
    driver=setup
    home_page = HomePage(driver)

    home_page.click_brand_option()

    assert home_page.verify_brand_logos()

def test_brand_popup(setup):
    driver = setup
    home_page = HomePage(driver)

    home_page.click_brand_popup()
    assert home_page.verify_all_products_same_brand()

def test_print_all_brands(setup):
    driver = setup
    home_page = HomePage(driver)

    home_page.hover(home_page.brand_option)
    home_page.print_all_brands()

def test_all_brands(setup):
    driver = setup
    home_page = HomePage(driver)

    home_page.hover(home_page.brand_option)

    brands = home_page.get_all_brands()

    for brand in brands:
        print("Checking brand:", brand)

        try:
            home_page.hover(home_page.brand_option)
            home_page.click_brand(brand)

            result = home_page.Verify_all_products_same_brand(brand)

            if not result:
                print("FAILED BRAND:", brand)

            driver.back()

        except Exception as e:
            print("FAILED TO OPEN BRAND:", brand)
            print("ERROR:", e)
            driver.back()