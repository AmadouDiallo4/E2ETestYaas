
from api.endpoints import HEALTH


def test_api_health(api_client):
    response = api_client.get(HEALTH)

    assert response.status_code == 200
    assert response.headers.get(
        "Content-Type", ""
    ).startswith("application/json")

    body = response.json()
    assert body["success"] is True
    assert "message" in body
