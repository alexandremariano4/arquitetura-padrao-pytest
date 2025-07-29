from dotenv import load_dotenv
from utils import driver
import os
import pytest

@pytest.fixture(scope="function")
def base_url():
    load_dotenv('.env')
    BASE_URL = os.getenv('BASE_URL')
    return BASE_URL
