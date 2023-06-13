from parallax_auth.models import ParallaxUser

from rest_framework import serializers


class ParallaxUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParallaxUser
        fields = ('email', 'is_staff', 'is_active')
