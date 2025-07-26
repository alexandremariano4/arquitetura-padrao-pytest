from helpers import (
    click_wait
)

class ProductDetailed:
    def __init__(self,driver):
        self.driver                          = driver
        self.VIEW_CART_BUTTON                = '.text-center > a[href*="view_cart"]'
        
    def view_cart(self):
        click_wait(self.driver,self.VIEW_CART_BUTTON)


