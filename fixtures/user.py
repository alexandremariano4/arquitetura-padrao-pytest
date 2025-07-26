from faker import Faker
import uuid

faker = Faker(locale='en_US')

class UserFactory:
    def __init__(self):
        self._first_name = faker.name()
        self._last_name = faker.last_name()
        self._full_name = self._first_name + ' ' + self._last_name
        self._email = f'{uuid.uuid4().hex[:8]}{faker.email(True)}'
        self._password = faker.password()
        self._company = faker.company()
        self._address = faker.address()
        self._zipcode = faker.zipcode()
        self._mobile_number = faker.phone_number()
    
    @property
    def full_name(self):
        return self._full_name
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email
    
    @property
    def password(self):
        return self._password
    
    @property
    def company(self):
        return self._company
    
    @property
    def address(self):
        return self._address
    
    @property
    def zipcode(self):
        return self._zipcode

    @property
    def mobile_number(self):
        return self._mobile_number