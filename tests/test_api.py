from http import HTTPStatus


def test_load_data(client):
    response = client.post(
        "/wines/load_data",
    )
    assert response.status_code == HTTPStatus.CREATED


def test_load_with_invalid_dataset(invalid_df_client_mocked_dataloader):
    response = invalid_df_client_mocked_dataloader.post(
        "/wines/load_data",
    )
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {
        "detail": "Dataset not available on kaggle to create the DB or you do not have permission"
    }


def test_health(client):
    response = client.get("/root/health")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "API Online"}


def test_hello(client):
    response = client.get("/root/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo Wine!"}
