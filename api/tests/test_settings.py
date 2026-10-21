
from api.endpoints import SETTINGS


def test_get_settings(api_client):
    response = api_client.get(SETTINGS)

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True
    assert isinstance(body["data"], dict)
