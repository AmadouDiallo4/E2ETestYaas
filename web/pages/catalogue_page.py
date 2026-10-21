
from selenium.webdriver.common.by import By

from web.pages.base_page import BasePage


class CataloguePage(BasePage):
    PRODUCTS_LINK = (
        By.CSS_SELECTOR,
        'nav#main-nav a[href="#produits"]',
    )
    PRODUCTS_SECTION = (By.ID, "produits")
    PRODUCTS_TITLE = (
        By.CSS_SELECTOR,
        "#produits .section-title",
    )
    FILTER_TABS = (By.CSS_SELECTOR, "#produits .filter-tabs")
    PRODUCTS_GRID = (By.ID, "products-grid")

    def open_products_section(self):
        self.click(self.PRODUCTS_LINK)
        self.wait_for_visible(self.PRODUCTS_SECTION)
        return self

    def get_products_title(self):
        return self.get_text(self.PRODUCTS_TITLE).strip()

    def is_products_grid_visible(self):
        return self.wait_for_visible(
            self.PRODUCTS_GRID
        ).is_displayed()

    def get_product_cards(self):
        return self.driver.find_elements(
            By.CSS_SELECTOR,
            "#products-grid > *",
        )
