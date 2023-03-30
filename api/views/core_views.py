from api.serializers.core_serializers import SubscriberSerializer
from rest_framework.generics import CreateAPIView


class SubscribeAPIView(CreateAPIView):
    serializer_class = SubscriberSerializer