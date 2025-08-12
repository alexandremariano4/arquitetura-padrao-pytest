from helpers import (
    click_wait,
    verify_element_presence
)
from components import Header

class HomePage:
    def __init__(self,driver):
        self.driver                 = driver
        self.signup_button          = Header(self.driver)
        self.CART_BUTTON            = 'i[class*="shopping-cart"]'

    def open_login_page(self):
        self.signup_button.open_signup_page()

    def open_cart_page(self):
        click_wait(self.driver,self.CART_BUTTON)
    
    def verify_page(self):
        verify_element_presence(self.driver,'img[alt="Website for automation practice"]')
