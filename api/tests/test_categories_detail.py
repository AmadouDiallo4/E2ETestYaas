
import pytest

from api.endpoints import CATEGORIES, CATEGORY_DETAIL


def test_get_existing_category(api_client):
    response = api_client.get(CATEGORIES)

    assert response.status_code == 200

    categories = response.json()["data"]

    if not categories:
        pytest.skip("Aucune catégorie disponible")

    category_id = categories[0]["id"]

    detail_response = api_client.get(
        CATEGORY_DETAIL.format(id=category_id)
    )

    assert detail_response.status_code == 200

    body = detail_response.json()

    assert body["success"] is True
    assert body["data"]["id"] == category_id
    assert isinstance(body["data"]["nom"], str)


def test_get_nonexistent_category(api_client):
    response = api_client.get(
        CATEGORY_DETAIL.format(id=999999999)
    )

    assert response.status_code == 404
