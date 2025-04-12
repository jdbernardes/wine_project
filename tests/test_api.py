from http import HTTPStatus

def test_load_data(client):
    response = client.post(
        '/wines/load_data',
    )
    assert response.status_code == HTTPStatus.CREATED
