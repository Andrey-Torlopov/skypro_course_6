from django.contrib.auth import get_user_model
from djoser.serializers import \
    UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers

User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
