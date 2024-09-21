from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'  # Include all fields

    
    # recipient_username = serializers.CharField(source='recipient.username', read_only=True)