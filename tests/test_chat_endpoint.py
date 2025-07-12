import pytest
from fastapi.testclient import TestClient
from pyagent.api.v1.endpoints.chat import router
from pyagent.models.chat import PostMessageRequest
from fastapi import FastAPI
from pyagent.services.gemini_service import GeminiService

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_post_message_success():
    class DummyGeminiService:
        def respond_to_chat(self, message):
            return "Hello, world!"

    app.dependency_overrides = {}
    app.dependency_overrides[GeminiService] = DummyGeminiService

    payload = {"message": "Hi"}
    response = client.post("/post-content", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Hello, world!"
    assert data["role"] == "model"

def test_post_message_missing_message():
    payload = {}
    response = client.post("/post-content", json=payload)
    assert response.status_code == 422 or response.status_code == 400

def test_post_message_service_error():
    class DummyGeminiService:
        def respond_to_chat(self, message):
            raise Exception("Service error!")

    app.dependency_overrides = {}
    from pyagent.services.gemini_service import GeminiService
    app.dependency_overrides[GeminiService] = DummyGeminiService

    payload = {"message": "Hi"}
    response = client.post("/post-content", json=payload)
    assert response.status_code == 500
    assert response.json()["detail"] == "Service error!"
