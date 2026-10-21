
from api.endpoints import PRODUCT_DETAIL


def test_get_existing_product(api_client):
    product_id = 66

    response = api_client.get(
        PRODUCT_DETAIL.format(id=product_id)
    )

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert body["data"]["id"] == product_id
    assert isinstance(body["data"]["nom"], str)
    assert isinstance(body["data"]["prix"], (int, float))


def test_get_nonexistent_product(api_client):
    response = api_client.get(
        PRODUCT_DETAIL.format(id=999999999)
    )

    assert response.status_code == 404
