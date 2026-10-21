
from Configs.environments import BASE_URL
from web.pages.catalogue_page import CataloguePage


def test_products_section_is_displayed(browser):
    browser.get(BASE_URL)

    catalogue = CataloguePage(browser)
    catalogue.open_products_section()

    assert catalogue.get_products_title() == "Nos produits"
    assert catalogue.is_products_grid_visible()


def test_products_grid_contains_products(browser):
    browser.get(BASE_URL)

    catalogue = CataloguePage(browser)
    catalogue.open_products_section()

    cards = catalogue.get_product_cards()

    assert len(cards) > 0, (
        "La grille des produits est vide ou les produits "
        "n'ont pas encore été chargés"
    )
