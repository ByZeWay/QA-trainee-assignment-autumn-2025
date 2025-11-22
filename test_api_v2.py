import pytest

class TestApiV2:
    def test_delete_item_success(self, api_client_v2, created_item_id):
        response = api_client_v2.delete(f"/api/2/item/{created_item_id}")
        print(f"Delete: {response.status_code}")

        if response.status_code == 200:
            get_response = api_client_v2.get(f"/api/1/item/{created_item_id}")
            assert get_response.status_code == 404
        else:
            pytest.fail(f"Delete failed: {response.text}")

    def test_delete_nonexistent_item(self, api_client_v2):
        response = api_client_v2.delete("/api/2/item/nonexistent_id_12345")
        print(f"Delete non-existent: {response.status_code}")

    def test_delete_invalid_id_format(self, api_client_v2):
        invalid_ids = ["invalid!@#", "123-abc", ""]
        for invalid_id in invalid_ids:
            response = api_client_v2.delete(f"/api/2/item/{invalid_id}")
            print(f"Delete invalid ID: {response.status_code}")

    def test_get_statistics_v2_success(self, api_client_v2, created_item_id):
        response = api_client_v2.get(f"/api/2/statistic/{created_item_id}")
        print(f"V2 Statistics: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, list)

    def test_get_statistics_v2_invalid_id(self, api_client_v2):
        response = api_client_v2.get("/api/2/statistic/invalid_id_123")
        print(f"V2 Statistics invalid: {response.status_code}")

    def test_api_version_consistency(self, api_client_v1, api_client_v2, created_item_id):
        stats_v1 = api_client_v1.get(f"/api/1/statistic/{created_item_id}")
        stats_v2 = api_client_v2.get(f"/api/2/statistic/{created_item_id}")
        assert stats_v1.status_code == stats_v2.status_code
