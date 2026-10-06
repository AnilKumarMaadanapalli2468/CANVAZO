"""
Base Page class containing common, reusable methods for all page objects.
This class is the foundation of the Page Object Model pattern.
"""

import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from utils.logger import get_logger
from selenium.webdriver.common.action_chains import ActionChains# Import our central logger utility

from selenium.webdriver.common.keys import Keys
from utils.logger import get_logger  # Import our central logger utility
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    """
    Base class for all page objects. Contains common methods that can be used
    across all page objects to maintain the DRY (Don't Repeat Yourself) principle.
    """

    def __init__(self, driver):
        """
        Initialize BasePage with the WebDriver instance and our central logger.
        """
        self.driver = driver
        # Explicit wait timeout can be configured here
        self.wait = WebDriverWait(driver, 20)
        # Use our central logger, already configured in conftest.py
        self.logger = get_logger()

    @allure.step("Clicking Element: {locator}")
    def click(self, locator):
        """
        Waits for an element to be clickable and then clicks it.
        Fails the test immediately if the element is not clickable within the timeout.
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Successfully clicked element: {locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not clickable: {locator}")
            # Re-raise the exception to fail the test and trigger failure evidence capture
            raise

    @allure.step("Entering text '{text}' into Element: {locator}")
    def send_keys(self, locator, text, clear_first=True):
        """
        Sends keys to an element after waiting for it to be visible.
        Fails the test immediately if the element is not found within the timeout.
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            if clear_first:
                element.clear()
            element.send_keys(text)
            self.logger.info(f"Successfully entered text into element: {locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Element not visible for text entry: {locator}")
            raise

    @allure.step("Checking if Element is visible: {locator}")
    def is_visible(self, locator, timeout=10):
        """
        Checks if an element is visible on the page within a given timeout.
        Returns True or False. Does not fail the test.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.logger.info(f"Element is visible: {locator}")
            return True
        except TimeoutException:
            self.logger.info(f"Element is not visible within {timeout}s: {locator}")
            return False

    @allure.step("Getting text from Element: {locator}")
    def get_text(self, locator):
        """
        Gets text from an element. Fails test if element not found.
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            text = element.text
            self.logger.info(f"Retrieved text '{text}' from element: {locator}")
            return text
        except TimeoutException:
            self.logger.error(f"Timeout: Could not get text from element as it was not visible: {locator}")
            raise

    @allure.step("Getting page title")
    def get_title(self):
        """Gets the title of the current page."""
        title = self.driver.title
        self.logger.info(f"Current page title: {title}")
        return title

    @allure.step("Navigating to URL: {url}")
    def navigate_to(self, url):
        """Navigates to a specific URL."""
        try:
            self.driver.get(url)
            self.logger.info(f"Successfully navigated to: {url}")
        except Exception as e:
            self.logger.error(f"Failed to navigate to {url}. Error: {e}")
            raise

    @allure.step("Accept Alert Popup")
    def accept_alert(self, timeout=10):
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            self.logger.info(f"Alert Message: {alert.text}")
            alert.accept()
            self.logger.info("Alert accepted successfully")
        except TimeoutException:
            self.logger.error("Alert did not appear")
            raise

    @allure.step("Press ENTER on Element: {locator}")
    def press_enter(self, locator):
        """
        Waits for the element to be visible and presses the ENTER key.
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator))
            element.send_keys(Keys.ENTER)
            self.logger.info(f"Pressed ENTER on element: {locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Could not press ENTER on element: {locator}")
            raise

    def move_to_element(self,locator):
        try:
            action=ActionChains(self.driver)
            ele=self.wait.until(EC.visibility_of_element_located(locator))
            action.move_to_element(ele).perform()
        except TimeoutException:
            self.logger.error(f"Timeout: Could not press ENTER on element: {locator}")
            raise

    def drop_down_single(self,locator):
        try:
            ele=self.wait.until(EC.element_to_be_clickable(locator))
            ele.click()
            obj=Select(ele)
            obj.select_by_index(0)
        except Exception as ec:
            self.logger.error(f"unable to select the element")
            raise

    def drop_down_multiple(self, dropdown_locator, options_locator):
        try:
            self.click(dropdown_locator)
            options = self.driver.find_elements(*options_locator)
            options[0].click()
            self.logger.info("First option selected successfully.")
        except Exception as e:
            self.logger.error(f"Unable to select the first option: {e}")
            raise

    def scroll_to_ele(self,locator):
        try:
            ele=self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth',block:'center'});",ele)
            self.logger.info("Successful scroll to element")
        except TimeoutException:
            self.logger.error("failed to scroll to the element")
            raise

    @allure.step("JavaScript Click on Element: {locator}")
    def js_click(self, locator):
        """
        Clicks an element using JavaScript executor.
        Useful when normal Selenium click fails due to overlays,
        hidden elements, or ElementClickInterceptedException.
        """
        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

            self.logger.info(f"Successfully clicked element using JavaScript: {locator}")

        except TimeoutException:
            self.logger.error(f"Timeout: Unable to JavaScript click element: {locator}")
            raise

    @allure.step("Performing action on Element: {locator}")
    def perform_action(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.logger.info(f"Successfully performed action on element: {locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Could not perform action on element: {locator}")
            raise

    @allure.step("Scrolling and clicking on Element: {locator}")
    def scroll_and_click(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            self.logger.info(f"Successfully scrolled and clicked on element: {locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Could not scroll and click on element: {locator}")
            raise

    @allure.step("Clicking on Element using JavaScript: {locator}")
    def js_click(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info(f"Successfully clicked on element using JavaScript: {locator}")
        except TimeoutException:
            self.logger.error(f"Timeout: Could not click on element using JavaScript: {locator}")
            raise


    @allure.step("Switch to window index: {index}")
    def switch_to_window(self, index):
        """
        Switches to the browser window/tab at the given index.
        Example:
            index=0 -> First window
            index=1 -> Second window
        """
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.window_handles) > index
            )

            self.driver.switch_to.window(self.driver.window_handles[index])
            self.logger.info(f"Switched to window at index {index}")

        except Exception as e:
            self.logger.error(f"Failed to switch to window {index}. Error: {e}")
            raise

    @allure.step("Hover on element: {locator}")
    def hover(self, locator):
        """
        Moves the mouse pointer over the specified element.
        Fails the test if the element is not visible within the timeout.
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            ActionChains(self.driver).move_to_element(element).perform()

            self.logger.info(f"Successfully hovered over element: {locator}")

        except TimeoutException:
            self.logger.error(f"Timeout: Unable to hover over element: {locator}")
            raise

    @allure.step("Move mouse to element: {locator}")
    def move_to_element(self, locator):
        """
        Moves the mouse pointer to the specified element without clicking.
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            ActionChains(self.driver).move_to_element(element).perform()

            self.logger.info(f"Successfully moved mouse to element: {locator}")

        except TimeoutException:
            self.logger.error(f"Timeout: Unable to move mouse to element: {locator}")
            raise

    @allure.step("Press Enter key on element: {locator}")
    def press_enter(self, locator):
        """
        Waits for an element to be visible and presses the Enter key.
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            element.send_keys(Keys.ENTER)

            self.logger.info(f"Successfully pressed ENTER on element: {locator}")

        except TimeoutException:
            self.logger.error(f"Timeout: Unable to press ENTER on element: {locator}")
            raise

    @allure.step("Close popup if present: {locator}")
    def click_if_present(self, locator, timeout=5):
        """
        Clicks an element if it appears. Does nothing if it doesn't.
        Does not fail the test if the element is not found.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            self.logger.info(f"Clicked optional element: {locator}")
        except TimeoutException:
            self.logger.info(f"Optional element not found: {locator}")

    @allure.step("Wait for page to load completely")
    def wait_for_page_load(self):
        self.wait.until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )
        self.logger.info("Page loaded successfully")

    @allure.step("Wait until custom condition is satisfied")
    def wait_until(self, condition, timeout=20):
        """
        Generic wait method.
        Usage:
            self.wait_until(lambda d: ...)
        """
        return WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Close popup using JavaScript")
    def close_popup_js(self, locator, timeout=8):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info("Popup closed using JavaScript.")
        except TimeoutException:
            self.logger.info("Popup not present.")

    @allure.step("Reload the current page")
    def reload_page(self):
        """
        Reload the current page.
        """
        self.driver.refresh()
        self.logger.info("Page reloaded successfully.")

    @allure.step("Verify element is visible. Reload page once if needed: {locator}")
    def is_visible_after_reload(self, locator, timeout=3):
        """
        Waits for an element.
        If not found within timeout, reloads the page once and waits again.
        Returns True if element is found, otherwise False.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.logger.info(f"Element is visible: {locator}")
            return True

        except TimeoutException:
            self.logger.warning(
                f"{locator} not found within {timeout}s. Reloading page..."
            )

            self.reload_page()

            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
                self.logger.info(f"Element is visible after reload: {locator}")
                return True

            except TimeoutException:
                self.logger.error(f"{locator} still not visible after reload.")
                return False