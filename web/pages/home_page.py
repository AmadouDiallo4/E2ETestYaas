
from selenium.webdriver.common.by import By

from Configs.environments import BASE_URL
from web.pages.base_page import BasePage


class HomePage(BasePage):
    BODY = (By.TAG_NAME, "body")
    SHOP_BUTTON = (
        By.XPATH,
        "//a[contains(normalize-space(), 'Découvrir la boutique')]"
        " | //button[contains(normalize-space(), 'Découvrir la boutique')]",
    )

    def open(self):
        self.open_url(BASE_URL)
        self.wait_for_visible(self.BODY)
        return self

    def get_title(self):
        return self.driver.title.strip()

    def get_body_text(self):
        return self.get_text(self.BODY).strip()

    def click_discover_shop(self):
        self.click(self.SHOP_BUTTON)
