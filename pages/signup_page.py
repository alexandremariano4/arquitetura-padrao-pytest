from helpers import (
    select_item,
    send_wait,
    click_wait,
    text_should_be
)

class SignupPage:
    def __init__(self,driver,user):
        self.user                        = user 
        self.driver                      = driver
        self.SIGNUP_HEADER_BUTTON        = 'a[href*="login"]'
        self.PRE_SIGNUP_NAME_FIELD       = 'input[data-qa="signup-name"]'
        self.PRE_SIGNUP_EMAIL_FIELD      = 'input[data-qa="signup-email"]'
        self.PRE_SIGNUP_BUTTON           = 'button[data-qa="signup-button"]'
        self.TITLE                       = 'input[value="Mrs"]'
        self.PASSWORD                    = 'input[data-qa="password"]'
        self.DAYS                        = 'select[data-qa="days"]'
        self.MONTHS                      = 'select[data-qa="months"]'
        self.YEARS                       = 'select[data-qa="years"]'
        self.FIRST_NAME                  = 'input[data-qa="first_name"]'
        self.LAST_NAME                   = 'input[data-qa="last_name"]'
        self.COMPANY                     = 'input[data-qa="company"]'
        self.ADDRESS                     = 'input[data-qa="address"]'
        self.COUNTRY                     = 'select[data-qa="country"]'
        self.STATE                       = 'input[data-qa="state"]'    
        self.CITY                        = 'input[data-qa="city"]'
        self.ZIPCODE                     = 'input[data-qa="zipcode"]'
        self.MOBILE_NUMBER               = 'input[data-qa="mobile_number"]'
        self.CREATE_ACCOUNT_BUTTON       = 'button[data-qa="create-account"]'
        self.ACCOUNT_CREATED_TEXT        = 'h2[data-qa="account-created"]'


    def full_signup(self):
        self.basic_signup()
        self.signup_user()

    def basic_signup(self):
        send_wait(
            driver=self.driver,
            element=self.PRE_SIGNUP_NAME_FIELD,
            text=self.user.full_name
            )
        send_wait(
            driver=self.driver,
            element=self.PRE_SIGNUP_EMAIL_FIELD,
            text=self.user.email
            )
        click_wait(
            driver=self.driver,
            element=self.PRE_SIGNUP_BUTTON,
            )

    def signup_user(self):
        click_wait(self.driver,self.TITLE)
        send_wait(self.driver,self.PASSWORD,self.user.password)
        select_item(self.driver,self.DAYS,'30')
        select_item(self.driver,self.MONTHS,'9')
        select_item(self.driver,self.YEARS,'1999')
        send_wait(self.driver,self.FIRST_NAME,self.user.first_name)
        send_wait(self.driver,self.LAST_NAME,self.user.last_name)
        send_wait(self.driver,self.COMPANY,self.user.company)
        send_wait(self.driver,self.ADDRESS,self.user.address)   
        select_item(self.driver,self.COUNTRY,'United States') 
        send_wait(self.driver,self.STATE,'Massachusetts')
        send_wait(self.driver,self.CITY,'Boston')
        send_wait(self.driver,self.ZIPCODE,self.user.zipcode)   
        send_wait(self.driver,self.MOBILE_NUMBER,self.user.mobile_number)
        click_wait(self.driver,self.CREATE_ACCOUNT_BUTTON)
        text_should_be(self.driver,self.ACCOUNT_CREATED_TEXT,text='Account Created!')
