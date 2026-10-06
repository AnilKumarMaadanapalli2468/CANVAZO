from time import sleep

from selenium.webdriver.common.by import By

from pages.Brand_Page import Brandpage


def test_brands_logo(setup):
    driver=setup
    home_page = Brandpage(driver)

    home_page.click_brand_option()

    assert home_page.verify_brand_logos()

def test_brand_popup(setup):
    driver = setup
    home_page = Brandpage(driver)

    home_page.click_brand_popup()
    assert home_page.verify_all_products_same_brand()

def test_print_all_brands(setup):
    driver = setup
    home_page = Brandpage(driver)

    home_page.hover(home_page.brand_option)
    home_page.print_all_brands()

def test_all_brands(setup):
    driver = setup
    home_page = Brandpage(driver)

    failed_brands = []

    home_page.hover(home_page.brand_option)
    brands = home_page.get_all_brands()

    for brand in brands:
        try:
            home_page.hover(home_page.brand_option)
            home_page.click_brand(brand)
            sleep(2)

            failed_products = home_page.Verify_all_products_same_brand(brand)

            if failed_products:
                failed_brands.append((brand, failed_products))

            driver.get("https://canvazo.com/")

        except Exception as e:
            failed_brands.append((brand, [f"Unable to open brand: {e}"]))
            driver.get("https://canvazo.com/")

    print("\n========== FAILED BRANDS ==========")

    for brand, products in failed_brands:
        print(f"\nBrand: {brand}")

        for product in products:
            print(f"FAILED PRODUCT: {product}")

    print("====================================")