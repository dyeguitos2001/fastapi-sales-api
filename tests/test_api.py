from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_list_sales():
    response = client.get("/sales")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_sales_summary():
    response = client.get("/sales/summary")
    assert response.status_code == 200
    body = response.json()
    assert "total_revenue" in body
    assert "total_orders" in body

def test_sales_by_region():
    response = client.get("/sales/region/Sudeste")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_sales_by_region_not_found():
    response = client.get("/sales/region/Atlantida")
    assert response.status_code == 404
