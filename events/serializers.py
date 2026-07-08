from rest_framework import serializers
from .models import LoginEvent

class LoginEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginEvent
        fields = ["id", "ip_address", "username", "status", "timestamp"]
        read_only_fields = ["id", "timestamp"]


