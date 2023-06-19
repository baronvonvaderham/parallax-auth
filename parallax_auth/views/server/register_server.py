from django.core.exceptions import ObjectDoesNotExist

from oauth2_provider.models import AccessToken
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from parallax_auth.models.server import Server
from parallax_auth.serializers.server import ServerSerializer


class RegisterServer(APIView):
    """
    View to register a new media server by a user.

    * Requires authenticated user (token authentication)
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request):
        """
        API endpoint for a user to register their new server.
        :param request:
            * access token: besides auth, required to pull the request's user
            * name: name of the server
            * client_id: client ID for the server instance
            * client_secret: client secret for the server instance
        :return:
        """
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]

        try:
            token_obj = AccessToken.objects.get(token=token)
        except ObjectDoesNotExist:
            return Response('Invalid access token provided', status=401)

        ip = request.META.get('REMOTE_ADDR')
        name = request.data.get('name')
        client_id = request.data.get('client_id')
        client_secret = request.data.get('client_secret')
        server = Server.objects.register(
            owner=token_obj.user,
            name=name,
            client_id=client_id,
            client_secret=client_secret,
            ip=ip,
        )
        return Response(data=ServerSerializer(instance=server).data)
