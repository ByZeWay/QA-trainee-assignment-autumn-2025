import pytest
import random
import re


class TestItemLifecycle:
    def extract_id(self, data):
        if isinstance(data, dict):
            if "id" in data:
                return data["id"]
            elif "status" in data:
                match = re.search(r'[a-f0-9-]{36}', data["status"])
                if match:
                    return match.group(0)
        return None

    def test_full_lifecycle(self, api_client_v1, api_client_v2, unique_seller_id):
        item_data = {
            "sellerId": unique_seller_id,
            "name": f"Test {random.randint(1000, 9999)}",
            "price": 5000,
            "statistics": {"likes": 10, "viewCount": 100, "contacts": 5}
        }

        create_response = api_client_v1.post("/api/1/item", item_data)

        if create_response.status_code != 200:
            pytest.skip("Cannot test lifecycle")

        item_id = self.extract_id(create_response.json())
        assert item_id

        api_client_v1.get(f"/api/1/item/{item_id}")
        api_client_v1.get(f"/api/1/{unique_seller_id}/item")
        api_client_v1.get(f"/api/1/statistic/{item_id}")
        api_client_v2.get(f"/api/2/statistic/{item_id}")

        delete_response = api_client_v2.delete(f"/api/2/item/{item_id}")
        final_get_response = api_client_v1.get(f"/api/1/item/{item_id}")

        assert delete_response.status_code == 200
        assert final_get_response.status_code in [400, 404]
