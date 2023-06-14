import pytest

from rest_framework.test import APIClient


def test_authorized_users__no_token(user, server):
    client = APIClient()
    response = client.get('/server/authorized-users/')
    assert response.status_code == 401


def test_authorized_users__just_owner(user, server, token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.token}')
    client.force_authenticate(user=user, token=token)
    response = client.get('/server/authorized-users/')
    print(response.data)
    assert response.status_code == 200
    assert response.data == ['feynman@caltech.edu']


def test_authorized_users__multiple(user, server, token, create_user):
    user2 = create_user(email='user2@domain.com')
    user3 = create_user(email='user3@domain.com')
    server.authorized_users.add(user2)
    server.authorized_users.add(user3)
    assert len(server.authorized_users.all()) == 2

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.token}')
    client.force_authenticate(user=user, token=token)
    response = client.get('/server/authorized-users/')
    print(response.data)
    assert response.status_code == 200
    assert len(response.data) == 3
