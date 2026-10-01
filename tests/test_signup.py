from pages.signup_page import Sign_Up

def test_sign_up(setup):
    driver = setup
    S = Sign_Up(driver)
    S.click_signup()
    S.click_email()
    S.enter_email_add('udaydayuday4@gmail.com')
    S.enter_pwd('Uday@123')
    S.enter_conf_pwd('Uday@123')
    S.click_check_box()
    S.click_continue()