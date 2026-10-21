
from api.endpoints import PRODUCTS


def test_get_products_returns_valid_response(api_client):
    response = api_client.get(
        PRODUCTS,
        params={"page": 1, "limit": 5}
    )

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert isinstance(body["items"], list)
    assert "pagination" in body

    for product in body["items"]:
        assert isinstance(product["id"], int)
        assert isinstance(product["nom"], str)
        assert isinstance(product["prix"], (int, float))


def test_get_products_respects_limit(api_client):
    response = api_client.get(
        PRODUCTS,
        params={"page": 1, "limit": 5}
    )

    assert response.status_code == 200

    body = response.json()

    assert len(body["items"]) <= 5
