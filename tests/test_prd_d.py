import pytest
from pages.prd_d_page import PrdDPage


class TestProductDetailsFlow:

    def test_complete_pdp_workflow(self, setup, wait):
        driver = setup
        pdp = PrdDPage(driver, wait)
        driver.get("https://canvazo.com/")
        pdp.navigate_to_paints_and_colors()
        assert pdp.is_pouring_medium_displayed(), "Pouring Medium product is not displayed"
        pdp.select_pouring_medium_product()
        assert pdp.is_product_title_displayed(), "Product title is not displayed"
        assert pdp.is_product_price_displayed(), "Product price is not displayed"
        pdp.select_500ml_size()
        pdp.increase_quantity()
        pdp.decrease_quantity()
        pdp.click_add_to_cart()
        assert pdp.is_product_added_to_cart(), "Failed to add Pouring Medium (500 ml) to cart"
        pdp.navigate_to_wooden_mannequins()
        assert pdp.is_mannequin_displayed(), "Mannequin product is not displayed"
        pdp.select_mannequin_product()
        assert pdp.is_out_of_stock_displayed(), "Out of stock / Sold Out message was not displayed for Wooden Mannequin"

'''import pytest
from pages.prd_d_page import PrdDPage


@pytest.fixture
def product_page(driver, wait):
    """Fixture to initialize PrdDPage instance."""
    return PrdDPage(driver, wait)


class TestProductDetail:

    def test_navigate_and_select_pouring_medium(self, product_page):
        """Verify navigation to Fluid Art and selection of Pouring Medium."""
        product_page.navigate_to_paints_and_colors()

        assert product_page.is_pouring_medium_displayed(), (
            "Pouring Medium product card was not found on the collection page."
        )

        product_page.select_pouring_medium_product()

        assert product_page.is_product_title_displayed(), (
            "Product Detail Page title is missing after selecting Pouring Medium."
        )
        assert product_page.is_product_price_displayed(), (
            "Product price is not displayed on the Product Detail Page."
        )

    def test_navigate_and_select_wooden_mannequin(self, product_page):
        """Verify navigation to Craft section and selection of Wooden Mannequin."""
        product_page.navigate_to_wooden_mannequins()

        assert product_page.is_mannequin_displayed(), (
            "Wooden Mannequin product card was not found on the collection page."
        )

        product_page.select_mannequin_product()

        assert product_page.is_product_title_displayed(), (
            "Product Detail Page title is missing after selecting Wooden Mannequin."
        )

    def test_quantity_increase_and_decrease(self, product_page):
        """Verify quantity selector increment and decrement functionality."""
        # Navigate directly to a known product page
        product_page.navigate_to_paints_and_colors()
        product_page.select_pouring_medium_product()

        initial_qty = product_page.get_quantity_value()

        # Increment
        product_page.increase_quantity()
        qty_after_inc = product_page.get_quantity_value()
        assert int(qty_after_inc) == int(initial_qty) + 1, (
            f"Expected quantity {int(initial_qty) + 1}, but got {qty_after_inc}"
        )

        # Decrement
        product_page.decrease_quantity()
        qty_after_dec = product_page.get_quantity_value()
        assert int(qty_after_dec) == int(initial_qty), (
            f"Expected quantity to return to {initial_qty}, but got {qty_after_dec}"
        )

    def test_add_product_to_cart(self, product_page):
        """Verify adding an item to cart and validating cart count/drawer."""
        product_page.navigate_to_paints_and_colors()
        product_page.select_pouring_medium_product()

        # Select variant if applicable
        product_page.select_500ml_size()

        # Handle out-of-stock guard rail
        if product_page.is_out_of_stock_displayed():
            pytest.skip("Product variant is currently out of stock.")

        product_page.click_add_to_cart()

        assert product_page.is_product_added_to_cart(), (
            "Product was not successfully added to cart (drawer/AJAX count check failed)."
        )'''