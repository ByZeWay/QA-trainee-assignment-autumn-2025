import requests
from typing import Dict, Optional

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def _make_request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return requests.request(method, url, **kwargs)

    def post(self, endpoint: str, json_data: Dict, headers: Optional[Dict] = None):
        if headers is None:
            headers = {"Content-Type": "application/json", "Accept": "application/json"}
        return self._make_request("POST", endpoint, json=json_data, headers=headers)

    def get(self, endpoint: str, headers: Optional[Dict] = None):
        if headers is None:
            headers = {"Accept": "application/json"}
        return self._make_request("GET", endpoint, headers=headers)

    def delete(self, endpoint: str, headers: Optional[Dict] = None):
        if headers is None:
            headers = {"Accept": "application/json"}
        return self._make_request("DELETE", endpoint, headers=headers)
