
from api.endpoints import PRODUCTS


def test_filter_products_by_search(api_client):
    response = api_client.get(
        PRODUCTS,
        params={"recherche": "THIOURAYE"}
    )

    assert response.status_code == 200

    body = response.json()
    assert body["success"] is True
    assert isinstance(body["items"], list)


def test_filter_products_by_category(api_client):
    response = api_client.get(
        PRODUCTS,
        params={"categorie": 7}
    )

    assert response.status_code == 200

    body = response.json()
    assert body["success"] is True
    assert isinstance(body["items"], list)


def test_filter_products_by_price(api_client):
    response = api_client.get(
        PRODUCTS,
        params={"prixMin": 0, "prixMax": 10000}
    )

    assert response.status_code == 200

    body = response.json()
    assert body["success"] is True
    assert isinstance(body["items"], list)
