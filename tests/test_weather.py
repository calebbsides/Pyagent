from fastapi.testclient import TestClient
from pyagent.app import app

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Healthy"}

def test_weather():
    response = client.get("/v1/weather")
    assert response.status_code == 200
    assert "temperature" in response.text or "London" in response.text
