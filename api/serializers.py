from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
    
from rest_framework import serializers
from .models import PremiumAccessLog

class PremiumAccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumAccessLog
        fields = "__all__"