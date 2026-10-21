
from api.endpoints import DASHBOARD, PRODUCTS


def test_dashboard_without_token(api_client):
    response = api_client.get(DASHBOARD)

    print("Dashboard HTTP:", response.status_code)
    print("Dashboard response:", response.text[:1000])

    assert response.status_code in (401, 403)


def test_products_invalid_page_diagnostic(api_client):
    response = api_client.get(
        PRODUCTS,
        params={"page": -1, "limit": 5}
    )

    print("Invalid page HTTP:", response.status_code)
    print("Invalid page response:", response.text[:1000])

    assert response.status_code in (200, 400, 422)
