import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TOP_ARTISTS:
    artists="//strong[text()='Top Artists']"
    arjith='//a[@aria-label="Arijit Singh" and @class="o-block__link"]'

    def __init__(self,setup):
        self.setup=setup
        self.wait = WebDriverWait(setup, 10)
    def click_on_top_artists(self):
        self.setup.find_element('xpath',self.artists).click()
        time.sleep(5)
    def click_on_arjith_singh(self):
        artist_arjith_ele=self.wait.until(EC.presence_of_element_located(('xpath',self.arjith)))
        artist_arjith_ele.click()
        time.sleep(3)