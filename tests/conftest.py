import pytest
from fastapi.testclient import TestClient
from kagglehub.exceptions import KaggleApiHTTPError
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from wine_project.app import app
from wine_project.database import get_session
from wine_project.data_loaders.dataset_loader import DatasetLoader
from wine_project.models.models import table_registry


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def invalid_df_client_mocked_dataloader(monkeypatch, session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override

    def mock_load_data(*args, **kwargs):
        raise KaggleApiHTTPError(message="Error")

    monkeypatch.setattr(DatasetLoader, "load_data", mock_load_data)

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()
