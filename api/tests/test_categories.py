
from api.endpoints import CATEGORIES


def test_get_categories(api_client):
    response = api_client.get(CATEGORIES)

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert isinstance(body["data"], list)
