from rest_framework import authentication
from rest_framework.views import APIView


class ClaimServer(APIView):
    """
    View to "claim" a new media server by a registered user.

    * Requires authenticated user (token authentication)
    """
    authentication_classes = [authentication.TokenAuthentication]

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
        ip = request.META.get('REMOTE_ADDR')
        # TODO: Finish fleshing out this endpoint
