import pytest
import random
import re

@pytest.fixture
def base_url():
    return "https://qa-internship.avito.com"

@pytest.fixture
def api_client_v1(base_url):
    from api_client import ApiClient
    return ApiClient(base_url)

@pytest.fixture
def api_client_v2(base_url):
    from api_client import ApiClient
    return ApiClient(base_url)

@pytest.fixture
def unique_seller_id():
    return random.randint(111111, 999999)

@pytest.fixture
def sample_item_data_v1(unique_seller_id):
    return {
        "sellerId": unique_seller_id,
        "name": f"Test Item {random.randint(1000, 9999)}",
        "price": random.randint(100, 10000),
        "statistics": {
            "likes": random.randint(0, 100),
            "viewCount": random.randint(0, 1000),
            "contacts": random.randint(0, 50)
        }
    }

@pytest.fixture
def sample_item_data_v2(unique_seller_id):
    return {
        "sellerId": unique_seller_id,
        "name": f"Test Item V2 {random.randint(1000, 9999)}",
        "price": random.randint(100, 10000)
    }

def extract_item_id(response_data):
    if isinstance(response_data, dict):
        if "id" in response_data:
            return response_data["id"]
        elif "status" in response_data:
            match = re.search(r'[a-f0-9-]{36}', response_data["status"])
            if match:
                return match.group(0)
    return None

@pytest.fixture
def created_item_id(api_client_v1, sample_item_data_v1):
    response = api_client_v1.post("/api/1/item", sample_item_data_v1)
    if response.status_code == 200:
        item_id = extract_item_id(response.json())
        if item_id:
            yield item_id
            try:
                api_client_v1.delete(f"/api/2/item/{item_id}")
            except:
                pass
        else:
            pytest.skip("Cannot extract item ID")
    else:
        pytest.skip(f"Cannot create test item: {response.text}")
