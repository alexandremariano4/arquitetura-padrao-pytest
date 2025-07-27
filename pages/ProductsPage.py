from helpers import (
    get_a_lot_elements,
    click_wait,text_should_be
)
import secrets

class ProductsPage:
    def __init__(self,driver):
        self.driver                          = driver
        self.ALL_PRODUCTS                    = '.features_items > .col-sm-4'
        self.PRODUCT_DETAILS                 = 'a[href*="product_details"]'
        self.CART_BUTTON                     = 'button[class*="cart"]'
        self.MODAL_SUCCESS_MESSAGE           = 'h4[class*="modal-title"]'
        self.PRODUCT_NAME                    = 'div[class*="productinfo"] > p'
        
        
    def choose_a_product(self):
        specific_product = secrets.choice(
            get_a_lot_elements(self.driver,self.ALL_PRODUCTS)
        )
        product_name = specific_product.find_element('css selector',self.PRODUCT_NAME).text
        url_product = specific_product.find_element('css selector',self.PRODUCT_DETAILS).get_attribute('href')
        self.driver.get(url_product)
        click_wait(self.driver,self.CART_BUTTON)
        text_should_be(self.driver, self.MODAL_SUCCESS_MESSAGE, 'Added!')
                
        return product_name
