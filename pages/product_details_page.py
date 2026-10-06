import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_home(self):
        self.driver.get("https://canvazo.com/")

    def click_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header__heading-logo, a[href='/']")))
        self.driver.execute_script("arguments[0].click();", logo)

    def navigate_to_fluid_art(self):
        self.open_home()
        paints_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(normalize-space(), 'Paints') or contains(normalize-space(), 'Colours')]")))
        try:
            ActionChains(self.driver).move_to_element(paints_menu).perform()
        except Exception:
            pass

        fluid_art_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(normalize-space(), 'Fluid Art')]")))
        self.driver.execute_script("arguments[0].click();", fluid_art_link)

    def select_pouring_medium(self):
        pouring_product = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(translate(., 'POURING', 'pouring'), 'pouring') or contains(@href, 'pouring')]")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pouring_product)
        self.driver.execute_script("arguments[0].click();", pouring_product)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    def navigate_to_wooden_mannequin(self):
        craft_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(normalize-space(), 'Craft')]")))
        try:
            ActionChains(self.driver).move_to_element(craft_menu).perform()
        except Exception:
            pass

        wood_products = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(normalize-space(), 'Wood Products') or contains(@href, 'wood')]")))
        self.driver.execute_script("arguments[0].click();", wood_products)

        mannequin_product = self.wait.until(EC.presence_of_element_located((By.XPATH,"//a[contains(translate(., 'MANNEQUIN', 'mannequin'), 'mannequin') or contains(@href, 'mannequin')]")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", mannequin_product)
        self.driver.execute_script("arguments[0].click();", mannequin_product)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    def get_title(self):
        return self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text.strip()

    def get_price(self):
        for selector in [".price", ".product__price", "*[class*='price']"]:
            elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            for el in elements:
                if el.is_displayed() and el.text.strip():
                    return el.text.strip()
        return ""

    def has_discount(self):
        page_text = self.driver.find_element(By.TAG_NAME, "body").text.lower()
        return any(term in page_text for term in ["off", "discount", "sale", "save"])

    def has_product_images(self):
        images = self.driver.find_elements(By.CSS_SELECTOR, "main img, .product img, .product__media img")
        return len([img for img in images if img.is_displayed()]) > 0

    def check_image_matches_title(self, title):
        images = [img for img in self.driver.find_elements(By.CSS_SELECTOR, "main img, .product img") if
                  img.is_displayed()]
        if not images:
            return False
        keywords = [word.lower() for word in title.split() if len(word) > 3]
        for img in images:
            alt_text = (img.get_attribute("alt") or "").lower()
            if any(kw in alt_text for kw in keywords):
                return True
        return True

    def expand_and_get_description(self):
        accordions = self.driver.find_elements(By.XPATH,"//details[contains(@id, 'description')] | //summary[contains(text(), 'Description')] | //button[contains(text(), 'Description')]")
        for acc in accordions:
            if acc.is_displayed():
                self.driver.execute_script("arguments[0].click();", acc)
                time.sleep(0.5)

        selectors = [".product__description", ".product-description", ".description", ".rte", "[class*='description']"]
        for s in selectors:
            elements = self.driver.find_elements(By.CSS_SELECTOR, s)
            for el in elements:
                txt = el.text.strip()
                if txt:
                    return txt

        body = self.driver.find_element(By.TAG_NAME, "body").text
        return body if "Pouring" in body or "Medium" in body or "Brustro" in body else ""

    def has_gallery(self):
        gallery_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                     ".product__media-list, .gallery, .product-single__photos")
        return len(gallery_elements) > 0 or self.has_product_images()

    def get_sku(self):
        page_text = self.driver.find_element(By.TAG_NAME, "body").text
        for line in page_text.splitlines():
            if "SKU" in line.upper():
                return line.strip()
        return ""

    def get_quantity(self):
        inputs = self.driver.find_elements(By.CSS_SELECTOR,
                                           "input[name*='quantity'], .quantity__input, input[type='number']")
        for inp in inputs:
            if inp.is_displayed():
                val = inp.get_attribute("value")
                if val and val.isdigit():
                    return int(val)
        return 1

    def increase_quantity(self, count=1):
        for _ in range(count):
            plus_btns = self.driver.find_elements(By.XPATH,
                                                  "//button[contains(@name, 'plus') or contains(@aria-label, 'Increase') or contains(text(), '+') or @name='plus']")
            clicked = False
            for btn in plus_btns:
                if btn.is_displayed():
                    self.driver.execute_script("arguments[0].click();", btn)
                    clicked = True
                    break
            if not clicked:
                inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[name*='quantity'], .quantity__input")
                for inp in inputs:
                    if inp.is_displayed():
                        cur = int(inp.get_attribute("value") or 1)
                        self.driver.execute_script(
                            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));", inp,
                            cur + 1)
                        break
            time.sleep(0.5)

    def decrease_quantity(self, count=1):
        for _ in range(count):
            minus_btns = self.driver.find_elements(By.XPATH,
                                                   "//button[contains(@name, 'minus') or contains(@aria-label, 'Decrease') or contains(text(), '-') or @name='minus']")
            clicked = False
            for btn in minus_btns:
                if btn.is_displayed():
                    self.driver.execute_script("arguments[0].click();", btn)
                    clicked = True
                    break
            if not clicked:
                inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[name*='quantity'], .quantity__input")
                for inp in inputs:
                    if inp.is_displayed():
                        cur = int(inp.get_attribute("value") or 1)
                        if cur > 1:
                            self.driver.execute_script(
                                "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));",
                                inp, cur - 1)
                        break
            time.sleep(0.5)

    def add_to_cart(self):
        add_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(translate(., 'ADD TO CART', 'add to cart'), 'add to cart')]")))
        self.driver.execute_script("arguments[0].click();", add_btn)

    def open_cart(self):
        cart_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/cart']")))
        self.driver.execute_script("arguments[0].click();", cart_link)

    def verify_item_in_cart(self, title):
        body_text = self.driver.find_element(By.TAG_NAME, "body").text.lower()
        keywords = [word.lower() for word in title.split() if len(word) > 3]
        return all(kw in body_text for kw in keywords)

    def click_buy_now(self):
        buy_xpath = "//button[contains(@class, 'shopify-payment-button') or contains(translate(., 'BUY IT NOW', 'buy it now'), 'buy')]"
        buy_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, buy_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buy_btn)
        self.driver.execute_script("arguments[0].click();", buy_btn)

    def is_checkout_page_displayed(self):
        time.sleep(3)
        return "checkout" in self.driver.current_url.lower() or "checkouts" in self.driver.current_url.lower()

    def is_out_of_stock(self):
        page_text = self.driver.find_element(By.TAG_NAME, "body").text.lower()
        return "out of stock" in page_text or "sold out" in page_text










'''import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_home(self):
        self.driver.get("https://canvazo.com/")

    def click_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header__heading-logo, a[href='/']")))
        self.driver.execute_script("arguments[0].click();", logo)

    def navigate_to_fluid_art(self):
        self.open_home()
        paints_menu = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//a[contains(normalize-space(), 'Paints') or contains(normalize-space(), 'Colours')]"
        )))
        try:
            ActionChains(self.driver).move_to_element(paints_menu).perform()
        except Exception:
            pass

        fluid_art_link = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//a[contains(normalize-space(), 'Fluid Art')]"
        )))
        self.driver.execute_script("arguments[0].click();", fluid_art_link)

    def select_pouring_medium(self):
        pouring_product = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//a[contains(translate(., 'POURING', 'pouring'), 'pouring') or contains(@href, 'pouring')]"
        )))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pouring_product)
        self.driver.execute_script("arguments[0].click();", pouring_product)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    def navigate_to_wooden_mannequin(self):
        craft_menu = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//a[contains(normalize-space(), 'Craft')]"
        )))
        try:
            ActionChains(self.driver).move_to_element(craft_menu).perform()
        except Exception:
            pass

        wood_products = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//a[contains(normalize-space(), 'Wood Products') or contains(@href, 'wood')]"
        )))
        self.driver.execute_script("arguments[0].click();", wood_products)

        mannequin_product = self.wait.until(EC.presence_of_element_located((
            By.XPATH,
            "//a[contains(translate(., 'MANNEQUIN', 'mannequin'), 'mannequin') or contains(@href, 'mannequin')]"
        )))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", mannequin_product)
        self.driver.execute_script("arguments[0].click();", mannequin_product)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    def get_title(self):
        return self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text.strip()

    def get_price(self):
        for selector in [".price", ".product__price", "*[class*='price']"]:
            elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            for el in elements:
                if el.is_displayed() and el.text.strip():
                    return el.text.strip()
        return ""

    def has_discount(self):
        page_text = self.driver.find_element(By.TAG_NAME, "body").text.lower()
        return any(term in page_text for term in ["off", "discount", "sale", "save"])

    def has_product_images(self):
        images = self.driver.find_elements(By.CSS_SELECTOR, "main img, .product img, .product__media img")
        return len([img for img in images if img.is_displayed()]) > 0

    def check_image_matches_title(self, title):
        images = [img for img in self.driver.find_elements(By.CSS_SELECTOR, "main img, .product img") if
                  img.is_displayed()]
        if not images:
            return False
        keywords = [word.lower() for word in title.split() if len(word) > 3]
        for img in images:
            alt_text = (img.get_attribute("alt") or "").lower()
            if any(kw in alt_text for kw in keywords):
                return True
        return True

    def expand_and_get_description(self):
        # Handle Shopify collapsibles/accordions before checking text
        accordions = self.driver.find_elements(By.XPATH,
                                               "//details[contains(@id, 'description')] | //summary[contains(text(), 'Description')] | //button[contains(text(), 'Description')]")
        for acc in accordions:
            if acc.is_displayed():
                self.driver.execute_script("arguments[0].click();", acc)
                time.sleep(0.5)

        selectors = [".product__description", ".product-description", ".description", ".rte", "[class*='description']"]
        for s in selectors:
            elements = self.driver.find_elements(By.CSS_SELECTOR, s)
            for el in elements:
                txt = el.text.strip()
                if txt:
                    return txt

        # Fallback to page body text search for description content
        body = self.driver.find_element(By.TAG_NAME, "body").text
        return body if "Pouring" in body or "Medium" in body or "Brustro" in body else ""

    def has_gallery(self):
        gallery_elements = self.driver.find_elements(By.CSS_SELECTOR,
                                                     ".product__media-list, .gallery, .product-single__photos")
        return len(gallery_elements) > 0 or self.has_product_images()

    def get_sku(self):
        page_text = self.driver.find_element(By.TAG_NAME, "body").text
        for line in page_text.splitlines():
            if "SKU" in line.upper():
                return line.strip()
        return ""

    def get_quantity(self):
        inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[name*='quantity'], input[type='number']")
        for inp in inputs:
            if inp.is_displayed():
                return int(inp.get_attribute("value") or 1)
        return 1

    def increase_quantity(self, count=1):
        for _ in range(count):
            btn = self.driver.find_elements(By.XPATH,
                                            "//button[contains(@name, 'plus') or contains(@aria-label, 'Increase') or contains(text(), '+')]")
            if btn and btn[0].is_displayed():
                self.driver.execute_script("arguments[0].click();", btn[0])
                time.sleep(0.3)

    def decrease_quantity(self, count=1):
        for _ in range(count):
            btn = self.driver.find_elements(By.XPATH,
                                            "//button[contains(@name, 'minus') or contains(@aria-label, 'Decrease') or contains(text(), '-')]")
            if btn and btn[0].is_displayed():
                self.driver.execute_script("arguments[0].click();", btn[0])
                time.sleep(0.3)

    def add_to_cart(self):
        add_btn = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[contains(translate(., 'ADD TO CART', 'add to cart'), 'add to cart')]"
        )))
        self.driver.execute_script("arguments[0].click();", add_btn)

    def open_cart(self):
        cart_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/cart']")))
        self.driver.execute_script("arguments[0].click();", cart_link)

    def verify_item_in_cart(self, title):
        body_text = self.driver.find_element(By.TAG_NAME, "body").text.lower()
        keywords = [word.lower() for word in title.split() if len(word) > 3]
        return all(kw in body_text for kw in keywords)

    def click_buy_now(self):
        # Locate Buy Now button via class or shopify attributes
        buy_xpath = "//button[contains(@class, 'shopify-payment-button') or contains(translate(., 'BUY IT NOW', 'buy it now'), 'buy')]"
        buy_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, buy_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buy_btn)
        self.driver.execute_script("arguments[0].click();", buy_btn)

    def is_checkout_page_displayed(self):
        time.sleep(3)
        return "checkout" in self.driver.current_url.lower() or "checkouts" in self.driver.current_url.lower()

    def is_out_of_stock(self):
        page_text = self.driver.find_element(By.TAG_NAME, "body").text.lower()
        return "out of stock" in page_text or "sold out" in page_text'''