import pytest

from rest_framework.test import APIClient


def test_register_server(user, user_token):
    data = {
        'name': 'API Created Test Server',
        'client_id': 'a totally valid client id',
        'client_secret': 'a super secret string',
    }
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {user_token.token}')
    client.force_authenticate(user=user, token=user_token)
    response = client.post('/server/register/', data=data)
    assert response.status_code == 200
    assert response.data.get('name') == data.get('name')
    assert response.data.get('ip') == '127.0.0.1'
    assert response.data.get('client_id') == data.get('client_id')
    # Client secret should NOT be included in response data
    assert response.data.get('client_secret') is None


def test_register_server__no_token(user):
    data = {
        'name': 'API Created Test Server',
        'client_id': 'a totally valid client id',
        'client_secret': 'a super secret string',
    }
    client = APIClient()
    response = client.post('/server/register/', data=data)
    assert response.status_code == 401


def test_register_server__token_in_wrong_place(user, user_token):
    data = {
        'name': 'API Created Test Server',
        'client_id': 'a totally valid client id',
        'client_secret': 'a super secret string',
    }
    client = APIClient()
    client.credentials(credentials=user_token.token)
    response = client.post('/server/register/', data=data)
    assert response.status_code == 401
    assert response.data.get('detail') == 'Authentication credentials were not provided.'


def test_authorized_users__invalid_token(user):
    data = {
        'name': 'API Created Test Server',
        'client_id': 'a totally valid client id',
        'client_secret': 'a super secret string',
    }
    token = 'A completely made up token'
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    client.force_authenticate(user=user, token=token)
    response = client.post('/server/register/', data=data)
    assert response.status_code == 401
