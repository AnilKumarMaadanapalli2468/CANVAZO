import time
class LOGIN:
    email='CustomerEmail'
    pwd='CustomerPassword'
    sign_in='(//button[@class="button black-btn btn-block"])[2]'

    def __init__(self, driver):
        self.driver = driver

    def pass_email(self,mail):
        self.driver.find_element('id', self.email).send_keys(mail)
        time.sleep(2)
    def pass_pwd(self,password):
        self.driver.find_element('id', self.pwd).send_keys(password)
        time.sleep(2)
    def click_sign_in(self):
        self.driver.find_element('xpath',self.sign_in).click()
        time.sleep(2)