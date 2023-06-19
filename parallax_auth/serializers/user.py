from parallax_auth.models import ParallaxUser

from rest_framework import serializers


class ParallaxUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    is_active = serializers.BooleanField()
    is_superuser = serializers.BooleanField()

    class Meta:
        model = ParallaxUser
        fields = ('email', 'is_staff', 'is_active', 'is_superuser')
