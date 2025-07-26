from helpers import (
    click_wait,
    text_should_be
)

class Header:
    def __init__(self,driver):
        self.driver = driver
        self.SIGNUP_BUTTON                   = 'a[href*="login"]'
        self.PRODUCTS_BUTTON                 = 'a[href*="products"] > i[class*="material-icons"]'
        self.LOGOUT_BUTTON                   = 'a[href*="logout"]'

    def open_signup_page(self):
        click_wait(self.driver,self.SIGNUP_BUTTON)

    def open_products_page(self):
        click_wait(self.driver,self.PRODUCTS_BUTTON)
    
    def loggout_user(self):
        click_wait(self.driver,self.LOGOUT_BUTTON)
    
    def verify_if_logged_out(self):
        text_should_be(self.driver,self.SIGNUP_BUTTON,'Signup / Login')