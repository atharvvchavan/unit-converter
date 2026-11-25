import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Unit Converter" in response.get_data(as_text=True)


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_version_has_a_value(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.get_json()


def test_api_converts(client):
    response = client.get("/api/convert?category=length&value=1&from=km&to=m")
    assert response.status_code == 200
    assert response.get_json()["result"] == 1000


def test_api_rejects_text_instead_of_number(client):
    response = client.get("/api/convert?category=length&value=abc&from=km&to=m")
    assert response.status_code == 400
    assert "number" in response.get_json()["error"]


def test_api_rejects_infinity(client):
    response = client.get("/api/convert?category=length&value=inf&from=km&to=m")
    assert response.status_code == 400


def test_api_rejects_unknown_unit(client):
    response = client.get("/api/convert?category=length&value=1&from=km&to=parsec")
    assert response.status_code == 400


def test_api_rejects_missing_value(client):
    response = client.get("/api/convert?category=length&from=km&to=m")
    assert response.status_code == 400
