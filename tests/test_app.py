import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "backend"))

from app import app


def test_home():
client = app.test_client()
response = client.get("/")

assert response.status_code == 200
assert response.get_json()["project"] == "SentinelHub"


def test_health():
client = app.test_client()
response = client.get("/events")

assert response.status_code == 200
assert "events" in response.get_json()

def test_root_message():
    client = app.test_client()
    response = client.get("/")

    data = response.get_json()

    assert data["status"] == "online"
    assert data["message"] == "SentinelHub backend is running"
