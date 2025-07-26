from helpers import (
    text_should_be
)

class AccountCreatedPage:
    def __init__(self,driver):
        self.driver                          = driver
        self.ACCOUNT_CREATED_TEXT            = 'h2[data-qa="account-created"]'

    def validate_account(self):
        text_should_be(self.driver,self.ACCOUNT_CREATED_TEXT,text='Account Created!')
