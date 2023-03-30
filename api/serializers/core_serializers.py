from core.models import Subscriber
from rest_framework import serializers


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'email',
            )