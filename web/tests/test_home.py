
from Configs.environments import BASE_URL
from web.pages.home_page import HomePage


def test_homepage_loads_successfully(browser):
    home_page = HomePage(browser).open()

    assert browser.current_url.startswith(BASE_URL), (
        "L'URL de la page d'accueil est incorrecte"
    )
    assert home_page.get_title(), (
        "Le titre de la page est vide"
    )
    assert home_page.get_body_text(), (
        "La page ne contient aucun texte"
    )
