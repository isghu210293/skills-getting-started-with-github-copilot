import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Fixture to provide a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def sample_activities():
    """Fixture to provide sample activity data for testing."""
    return {
        "Chess Club": {
            "description": "Learn chess strategies",
            "schedule": "Mondays 4-5 PM",
            "max_participants": 20,
            "participants": []
        },
        "Programming Class": {
            "description": "Introduction to programming",
            "schedule": "Tuesdays 3-4 PM",
            "max_participants": 15,
            "participants": ["student1@example.com"]
        }
    }