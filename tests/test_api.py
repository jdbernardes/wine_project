from http import HTTPStatus

def test_load_data(client):
    response = client.post(
        '/wines/load_data',
    )
    assert response.status_code == HTTPStatus.CREATED

def test_health(client):
    response = client.get(
        '/root/health'
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'API Online'}

def test_hello(client):
    response = client.get(
        '/root/'
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo Wine!'}
