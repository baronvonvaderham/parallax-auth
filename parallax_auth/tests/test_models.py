import pytest

from django.core.exceptions import FieldError

from parallax_auth.models.server import Server
from parallax_auth.models.user import ParallaxUser


class TestUserModel:

    def test_create_user(self):
        user = ParallaxUser.objects.create_user(
            email='feynman@caltech.edu',
            password='password',
        )
        assert isinstance(user, ParallaxUser)
        assert user.email == 'feynman@caltech.edu'
        assert user.__str__() == 'feynman@caltech.edu'

    def test_create_superuser(self):
        user = ParallaxUser.objects.create_superuser(
            email='feynman@caltech.edu',
            password='password',
        )
        assert isinstance(user, ParallaxUser)
        assert user.email == 'feynman@caltech.edu'
        assert user.is_superuser
        assert user.is_staff

    def test_delete_user(self, user):
        assert isinstance(user, ParallaxUser)
        assert user.deleted_at is None
        user.delete()
        assert isinstance(user, ParallaxUser)
        assert user.deleted_at is not None


class TestServerModel:

    def test_register_server(self, user):
        server = Server.objects.register(
            owner=user,
            name='Test Server',
            client_id='totally valid client id',
            client_secret='something an idiot would have on his luggage'
        )
        assert isinstance(server, Server)
        assert server.authorization_grant_type == 'client-credentials'
        assert server.ip is None
        assert server.client_id == 'totally valid client id'
        assert server.owner == user

    def test_register_server__missing_data(self, user):
        with pytest.raises(FieldError) as e:
            server = Server.objects.register(
                owner=user,
                name='Test Server',
                client_id='totally valid client id',
                client_secret=None
            )

    def test_add_authorized_user_to_server(self, server, user):
        assert len(server.authorized_users.all()) == 0
        server.add_authorized_user(user)
        assert len(server.authorized_users.all()) == 1
