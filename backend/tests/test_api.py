import pytest
from fastapi.testclient import TestClient
from .app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Striker2.1 AI Creative Studio API"}

def test_list_providers():
    response = client.get("/providers")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["id"] == "demo"

def test_create_project():
    # Use a dummy key for auth
    headers = {"x-api-key": "striker-secret-key"}
    payload = {"user_id": 1, "name": "Test Project", "description": "First project"}
    response = client.post("/projects", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Project"
