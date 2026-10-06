import time
import pytest
from pages.product_details_page import ProductDetailsPage

@pytest.mark.usefixtures("setup")
class TestProductDetails:

    @pytest.fixture(autouse=True)
    def init_page(self, setup):
        self.driver = setup
        self.pdp = ProductDetailsPage(self.driver)

    def test_pouring_medium_flow_and_details(self):
        self.pdp.navigate_to_fluid_art()
        self.pdp.select_pouring_medium()
        title = self.pdp.get_title()
        assert title, "Product title is missing"
        assert "pouring" in title.lower() or "medium" in title.lower() or "brustro" in title.lower()
        assert self.pdp.get_price(), "Price is missing"
        assert self.pdp.has_product_images(), "Product images not displayed"
        assert self.pdp.check_image_matches_title(title), "Image alt text does not match title"
        desc = self.pdp.expand_and_get_description()
        assert desc != "", "Description is missing"
        assert self.pdp.has_gallery(), "Gallery is not displayed"
        initial_qty = self.pdp.get_quantity()
        self.pdp.increase_quantity(3)
        time.sleep(1)
        assert self.pdp.get_quantity() == initial_qty + 3
        self.pdp.decrease_quantity(1)
        time.sleep(1)
        assert self.pdp.get_quantity() == initial_qty + 2
        self.pdp.add_to_cart()
        self.pdp.open_cart()
        assert self.pdp.verify_item_in_cart(title), "Product missing from cart"

    def test_pouring_medium_buy_now_checkout(self):
        self.pdp.navigate_to_fluid_art()
        self.pdp.select_pouring_medium()
        self.pdp.click_buy_now()
        assert self.pdp.is_checkout_page_displayed(), "Checkout page was not displayed after clicking Buy Now"

    def test_wooden_mannequin_details_and_stock(self):
        self.pdp.open_home()
        self.pdp.click_logo()
        self.pdp.navigate_to_wooden_mannequin()
        title = self.pdp.get_title()
        assert title, "Mannequin title is missing"
        assert "mannequin" in title.lower()
        assert self.pdp.has_product_images(), "Mannequin images missing"
        description = self.pdp.expand_and_get_description()
        print(f"Mannequin Description Content: '{description}'")
        assert self.pdp.has_gallery(), "Gallery missing"
        assert self.pdp.is_out_of_stock(), "Expected Wooden Mannequin to be marked out of stock"









'''import pytest
from pages.product_details_page import ProductDetailsPage


@pytest.mark.usefixtures("setup")
class TestProductDetails:

    @pytest.fixture(autouse=True)
    def init_page(self, setup):
        self.driver = setup
        self.pdp = ProductDetailsPage(self.driver)

    def test_pouring_medium_flow_and_details(self):
        # 1. Hover Paints & Colours -> Select Fluid Art
        self.pdp.navigate_to_fluid_art()

        # 2. Select Pouring Medium product
        self.pdp.select_pouring_medium()

        # 3. Verify details
        title = self.pdp.get_title()
        assert title, "Product title is missing"
        assert "pouring" in title.lower() or "medium" in title.lower() or "brustro" in title.lower()

        assert self.pdp.get_price(), "Price is missing"
        assert self.pdp.has_product_images(), "Product images not displayed"
        assert self.pdp.check_image_matches_title(title), "Image alt text does not match title"

        # Expanded description fetch check
        desc = self.pdp.expand_and_get_description()
        assert desc != "", "Description is missing"

        assert self.pdp.has_gallery(), "Gallery is not displayed"

        # 4. Quantity Adjustments (Increase by 3, Decrease by 1)
        initial_qty = self.pdp.get_quantity()
        self.pdp.increase_quantity(3)
        assert self.pdp.get_quantity() == initial_qty + 3

        self.pdp.decrease_quantity(1)
        assert self.pdp.get_quantity() == initial_qty + 2

        # 5. Add to Cart & Verify Cart
        self.pdp.add_to_cart()
        self.pdp.open_cart()
        assert self.pdp.verify_item_in_cart(title), "Product missing from cart"

    def test_pouring_medium_buy_now_checkout(self):
        # Come back to Pouring Medium product and test Buy Now -> Checkout
        self.pdp.navigate_to_fluid_art()
        self.pdp.select_pouring_medium()

        self.pdp.click_buy_now()
        assert self.pdp.is_checkout_page_displayed(), "Checkout page was not displayed after clicking Buy Now"

    def test_wooden_mannequin_details_and_stock(self):
        # 1. Click Logo to return home
        self.pdp.open_home()
        self.pdp.click_logo()

        # 2. Hover Craft -> Select Wood Products -> Select 12 Inch Wooden Mannequin
        self.pdp.navigate_to_wooden_mannequin()

        # 3. Verify details & Out of stock status
        title = self.pdp.get_title()
        assert title, "Mannequin title is missing"
        assert "mannequin" in title.lower()

        assert self.pdp.has_product_images(), "Mannequin images missing"

        description = self.pdp.expand_and_get_description()
        print(f"Mannequin Description Content: '{description}'")

        assert self.pdp.has_gallery(), "Gallery missing"
        assert self.pdp.is_out_of_stock(), "Expected Wooden Mannequin to be marked out of stock"'''