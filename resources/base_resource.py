from helpers import *
from fixtures import UserFactory
from components import Header
from pages import *


class PageFunctions:
    def __init__(self,driver):
        self._header                  = Header(driver)
        self._signup_page             = SignupPage(driver,UserFactory())   
        self._account_created_page    = AccountCreatedPage(driver)
        self._products_page           = ProductsPage(driver)
        self._product_detailed        = ProductDetailed(driver)
        self._cart                    = Cart(driver)
        self._home_page               = HomePage(driver)
    
    @property
    def header(self):
        return self._header
    
    @property
    def signup_page(self):
        return self._signup_page
    
    @property
    def account_created(self):
        return self._account_created_page
    
    @property
    def products_page(self):
        return self._products_page
    
    @property
    def product_detailed(self):
        return self._product_detailed
    
    @property
    def cart_page(self):
        return self._cart
    
    @property
    def home_page(self):
        return self._home_page
