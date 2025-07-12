import pytest
from fastapi.testclient import TestClient
from pyagent.api.v1.endpoints.chat import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_post_message_success(client, monkeypatch):
    def mock_respond_to_chat(chat_history):
        return "Hello!"
    monkeypatch.setattr("pyagent.api.v1.endpoints.chat.respond_to_chat", mock_respond_to_chat)
    payload = {"chat_history": [{"role": "user", "text": "Hi"}]}
    response = client.post("/messages", json=payload)
    assert response.status_code == 200
    assert response.json() == {"text": "Hello!"}

def test_post_message_missing_history(client):
    payload = {}
    response = client.post("/messages", json=payload)
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Field required"

def test_post_message_empty_history(client):
    payload = {"chat_history": []}
    response = client.post("/messages", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Chat history required."

def test_post_message_internal_error(client, monkeypatch):
    def fail_respond_to_chat(chat_history):
        raise Exception("fail")
    monkeypatch.setattr("pyagent.api.v1.endpoints.chat.respond_to_chat", fail_respond_to_chat)
    payload = {"chat_history": [
        {"role": "user", "text": "Hi"},
        {"role": "model", "text": "How are you?"}
    ]}
    response = client.post("/messages", json=payload)
    assert response.status_code == 500
    assert "fail" in response.json()["detail"]
