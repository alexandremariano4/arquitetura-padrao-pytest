from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv
import pytest

@pytest.fixture(scope="function")
def driver():
        browser_option = ChromeOptions()
        browser_option.page_load_strategy = 'eager'
        browser_option.add_argument("window-size=2000x1500")
        browser_option.add_argument("--log-level=3")
        browser_option.add_argument("--headless=new")

        services = Service(
            ChromeDriverManager().install(),            
            )

        driver = Chrome(
            options=browser_option,
            service=services
            )
        driver.maximize_window()
        yield driver
        driver.close()
        
@pytest.fixture(scope="function")
def base_url():
    load_dotenv('.env')
    BASE_URL = os.getenv('BASE_URL')
    return BASE_URL
