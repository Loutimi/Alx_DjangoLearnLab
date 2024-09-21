from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Notification
from .serializers import NotificationSerializer

class CreateNotificationView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Get data from request (assuming data contains recipient, actor, verb, and target)
        data = self.request.data
        recipient = data.get('recipient')
        actor = self.request.user
        verb = data.get('verb')
        target = data.get('target')

        # Validate data (optional)

        serializer.save(recipient=recipient, actor=actor, verb=verb, target=target)


class GetNotificationsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(recipient=user).order_by('-timestamp')


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        for notification in queryset:
            notification.is_read = True
            notification.save()
        return super().list(request, *args, **kwargs)
