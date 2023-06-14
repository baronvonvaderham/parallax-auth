from rest_framework import authentication
from rest_framework.views import APIView


class ClaimServer(APIView):
    """
    View to "claim" a new media server by a registered user.

    * Requires authenticated user (token authentication)
    """
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        pass
