import pytest

from rest_framework.test import APIClient


def test_authorized_users__no_token(user, server):
    client = APIClient()
    response = client.get('/server/authorized-users/')
    assert response.status_code == 401
    assert response.data.get('detail') == 'Authentication credentials were not provided.'


def test_authorized_users__post(user, server, server_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {server_token.token}')
    client.force_authenticate(user=user, token=server_token)
    response = client.post('/server/authorized-users/')
    assert response.status_code == 405


def test_authorized_users__token_in_wrong_place(user, server, server_token):
    client = APIClient()
    client.credentials(credentials=server_token.token)
    response = client.get('/server/authorized-users/')
    assert response.status_code == 401
    assert response.data.get('detail') == 'Authentication credentials were not provided.'


def test_authorized_users__just_owner(user, server, server_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {server_token.token}')
    client.force_authenticate(user=user, token=server_token)
    response = client.get('/server/authorized-users/')
    assert response.status_code == 200
    assert response.data == ['feynman@caltech.edu']


def test_authorized_users__multiple(user, server, server_token, create_user):
    user2 = create_user(email='user2@domain.com')
    user3 = create_user(email='user3@domain.com')
    server.authorized_users.add(user2)
    server.authorized_users.add(user3)
    assert len(server.authorized_users.all()) == 2

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {server_token.token}')
    client.force_authenticate(user=user, token=server_token)
    response = client.get('/server/authorized-users/')
    assert response.status_code == 200
    assert len(response.data) == 3


def test_authorized_users__invalid_token(user, server):
    token = 'A completely made up token'
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    client.force_authenticate(user=user, token=token)
    response = client.get('/server/authorized-users/')
    assert response.status_code == 401
