
from api.endpoints import DASHBOARD, AUTH_ME, ADMIN_ORDERS


def test_dashboard_without_token(api_client):
    response = api_client.get(DASHBOARD)

    assert response.status_code in (401, 403)


def test_admin_profile_without_token(api_client):
    response = api_client.get(AUTH_ME)

    assert response.status_code in (401, 403)


def test_admin_orders_without_token(api_client):
    response = api_client.get(ADMIN_ORDERS)

    assert response.status_code in (401, 403)
