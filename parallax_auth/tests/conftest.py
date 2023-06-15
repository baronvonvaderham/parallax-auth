import pytest

from model_bakery import baker


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture
def create_user():
    """
    A function to create ParallaxUser instances.
    """
    from parallax_auth.models.user import ParallaxUser

    def _create_user(**kwargs):
        return baker.make(ParallaxUser, **kwargs)
    return _create_user


@pytest.fixture
def user(create_user):
    """
    A ParallaxUser instance for a generic default user
    """
    return create_user(
        email='feynman@caltech.edu'
    )


@pytest.fixture
def create_server():
    """
    A function to create Server instances
    """
    from parallax_auth.models.server import Server

    def _create_server(**kwargs):
        return baker.make(Server, **kwargs)
    return _create_server


@pytest.fixture
def server(create_server, user):
    """
    A Server instance for a default generic server owned by the default user
    """
    return create_server(
        user=user,
        name='My Test Server',
    )


@pytest.fixture
def create_token(server):
    """
    A function to create AccessToken instances
    """
    from oauth2_provider.models import AccessToken

    def _create_token(server=server, **kwargs):
        return baker.make(AccessToken, application=server, **kwargs)
    return _create_token


@pytest.fixture
def token(create_token):
    """
    An AccessToken instance for a default token for the default server
    """
    return create_token()
