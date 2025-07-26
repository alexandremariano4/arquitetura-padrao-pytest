from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from assertpy import assert_that
from .log_decorator import log_on_exception

TIME = 5
TYPE_LOCATOR = By.CSS_SELECTOR

@log_on_exception
def click_wait(driver,element,time=TIME,type_locator=TYPE_LOCATOR):
    WebDriverWait(driver,time).until(EC.visibility_of_element_located((type_locator,element))).click()

@log_on_exception
def send_wait(driver,element,text,time=TIME,type_locator=TYPE_LOCATOR):
    WebDriverWait(driver,time).until(EC.visibility_of_element_located((type_locator,element))).clear()
    WebDriverWait(driver,time).until(EC.visibility_of_element_located((type_locator,element))).send_keys(text)

@log_on_exception
def verify_element_presence(driver,element,time=TIME,type_locator=TYPE_LOCATOR):
    WebDriverWait(driver,time).until(EC.visibility_of_element_located((type_locator,element)))

@log_on_exception
def select_item(driver,element,value,time=TIME,type_locator=TYPE_LOCATOR):
    Select(
        WebDriverWait(driver,time)
            .until(EC.visibility_of_element_located(
                        (type_locator,element)
                    )
                )
            ).select_by_value(value)

@log_on_exception
def text_should_be(driver, element, text, time=TIME, type_locator=TYPE_LOCATOR):
        assert_that(
            WebDriverWait(driver, time).until(EC.visibility_of_element_located((type_locator, element))).text.upper().strip(),
            'Element text are different than expected'
        ).is_equal_to(text.upper())

@log_on_exception
def get_a_lot_elements(driver, element, time=TIME, type_locator=TYPE_LOCATOR):
    element = WebDriverWait(driver, time).until(EC.visibility_of_all_elements_located((type_locator, element)))
    return element

@log_on_exception
def get_element(driver, element, time=TIME, type_locator=TYPE_LOCATOR):
    element = WebDriverWait(driver, time).until(EC.visibility_of_element_located((type_locator, element)))
    return element



