from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


def test_main(client: TestClient, db: Session) -> None:
    """Test if base url in fast api is responding."""
    response = client.get("/")
    assert response.status_code == 200
    content = response.json()
    assert content["Hello"] == "World"
