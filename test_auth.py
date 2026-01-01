import json
import os
from fastapi.testclient import TestClient
from main import app   

client = TestClient(app)

def test_register_existing_user():
    response = client.post("/register", json={
        "username": "testuser",
        "email": "test@gmail.com",
        "password": "123456"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already exists"


def test_login_success():
    response = client.post("/login", json={
        "username": "testuser",
        "password": "123456"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"


def test_login_wrong_password():
    response = client.post("/login", json={
        "username": "testuser",
        "password": "wrongpassword"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Incorrect password"


def test_login_user_not_found():
    response = client.post("/login", json={
        "username": "ghost",
        "password": "123456"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "User not found"
