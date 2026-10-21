
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from api.client import ApiClient
from Configs.environments import BROWSER_WINDOW_SIZE

@pytest.fixture(scope="session")
def api_client():
    client = ApiClient()

    yield client

    client.close()

@pytest.fixture
def browser():
    options = Options()
    options.add_argument(f"--window-size={BROWSER_WINDOW_SIZE}")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
