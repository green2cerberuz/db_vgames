from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


def test_main(fast_api_client: TestClient, db: Session) -> None:
    """Test if base url in fast api is responding."""
    response = fast_api_client.get("/")
    assert response.status_code == 200
    content = response.json()
    assert content["Hello"] == "World"
