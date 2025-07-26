from resources import (
    PageFunctions
)

def test_expect_that_homepage_is_open(driver,base_url):
    driver.get(base_url)
    p = PageFunctions(driver)
    
    p.home_page.verify_page()
    p.header.open_signup_page()
    p.signup_page.full_signup()
    p.account_created.validate_account()
    p.header.open_products_page()
    product_name = p.products_page.choose_a_product()
    p.product_detailed.view_cart()
    p.cart_page.validate_product_name(product_name)
    p.cart_page.delete_product()
    p.cart_page.validate_empty_cart()
    p.header.loggout_user()
    p.header.verify_if_logged_out()
