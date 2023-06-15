from django.core.exceptions import ObjectDoesNotExist

from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from oauth2_provider.models import AccessToken


class AuthorizedUsers(APIView):
    """
    View to return a list of authorized users who have permissions to access a server.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        try:
            token_obj = AccessToken.objects.get(token=token)
            owner = token_obj.application.user.email
            users = [user.email for user in token_obj.application.authorized_users.all()]
            users.append(owner)
            return Response(list(set(users)))
        except ObjectDoesNotExist:
            return Response('Invalid access token provided', status=401)
