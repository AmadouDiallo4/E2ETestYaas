
from selenium.webdriver.support.ui import WebDriverWait

from Configs.environments import BASE_URL
from web.pages.home_page import HomePage


def test_discover_shop_button_navigation(browser):
    home_page = HomePage(browser).open()

    home_page.click_discover_shop()

    WebDriverWait(browser, 10).until(
        lambda driver: driver.current_url != BASE_URL
        or "#categories" in driver.current_url.lower()
    )

    assert (
        "#categories" in browser.current_url.lower()
        or browser.current_url.rstrip("/") != BASE_URL.rstrip("/")
    ), "Le bouton ne semble pas avoir ouvert la boutique"
