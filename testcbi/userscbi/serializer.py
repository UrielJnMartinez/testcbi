from rest_framework import serializers

from .models import UserCBI

class UserSerializer(serializers.Serializer):
    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return UserCBI.objects.create(**validated_data)

    def update(self,instance,validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        
        instance.save()
        return instance