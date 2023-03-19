from rest_framework import serializers
from base.models import Client
from django.contrib.auth.models import User


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields ='__all__'


# class UserSerializer(serializers.ModelSerializer):
#        class Meta:
#            model = User
#            field='__all__'
