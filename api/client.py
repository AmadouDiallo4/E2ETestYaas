
import requests

from api.config import BASE_URL, TIMEOUT


class ApiClient:

    def __init__(self):
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        url = f"{BASE_URL.rstrip('/')}/{endpoint.lstrip('/')}"

        return self.session.get(
            url,
            timeout=TIMEOUT,
            **kwargs
        )

    def close(self):
        self.session.close()
