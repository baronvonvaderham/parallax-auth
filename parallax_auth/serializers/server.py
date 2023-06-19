from rest_framework import serializers

from parallax_auth.models.server import Server
from parallax_auth.serializers.user import ParallaxUserSerializer


class ServerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=32)
    ip = serializers.IPAddressField()
    client_id = serializers.CharField(max_length=100)

    class Meta:
        model = Server
        fields = ('name', 'ip', 'client_id', 'authorized_users')
