from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Sign_Up:
    sign_up = ('id','signup')
    email = ('xpath',"//span[text()='Email']")
    email_addres = ('id',"email")
    pwd = ('id','password')
    conf_pwd = ('id','confirmpassword')
    check_box = ('xpath','//div[@id="rc-anchor-over-quota"]')
    contu_but = ('xpath','//button[@type="submit"]')

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)

    def click_signup(self):
        click_sign = self.wait.until(EC.element_to_be_clickable((self.sign_up)))
        click_sign.click()

    def click_email(self):
        click_email = self.wait.until(EC.element_to_be_clickable(self.email))
        click_email.click()

    def enter_email_add(self,email_address):
        click_mail_add = self.wait.until(EC.element_to_be_clickable((self.email_addres)))
        click_mail_add.send_keys(email_address)

    def enter_pwd(self,password):
        click_pwd = self.wait.until(EC.element_to_be_clickable((self.pwd)))
        click_pwd.send_keys(password)

    def enter_conf_pwd(self,confirm_pwd):
        click_confpwd = self.wait.until(EC.element_to_be_clickable((self.conf_pwd)))
        click_confpwd.send_keys(confirm_pwd)

    def click_check_box(self):
        Click_checkbox = self.wait.until(EC.visibility_of_all_elements_located((self.check_box)))
        Click_checkbox.click()

    def click_continue(self):
        click_conti = self.wait.until(EC.element_to_be_clickable((self.contu_but)))
        click_conti.click()