from helpers import (
    text_should_be,
    click_wait
)

class Cart:
    def __init__(self,driver):
        self.driver                          = driver
        self.ELEMENT_PRODUCT_NAME            = '.cart_description > h4 > a'
        self.REMOTE_BUTTON                   = '.cart_quantity_delete'  
        
    def validate_product_name(self,product_name):
        text_should_be(self.driver,self.ELEMENT_PRODUCT_NAME,product_name)

    def delete_product(self):
        click_wait(self.driver,self.REMOTE_BUTTON)

    def validate_empty_cart(self):
        text_should_be(self.driver,'.text-center > b','Cart is empty!')