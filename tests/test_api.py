# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_coins():
    response = client.get("/api/v1/coins?page_num=1&per_page=5")
    assert response.status_code == 200
    assert len(response.json()) == 5