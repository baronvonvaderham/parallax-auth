import pytest


def test_add_authorized_user(server, user, create_user):
    assert len(server.authorized_users.all()) == 0
    server.authorized_users.add(user)
    assert len(server.authorized_users.all()) == 1
