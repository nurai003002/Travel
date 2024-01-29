from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.hotels.models import Hotel
from apps.hotels.serializers import HotelSerializer

class HotelAPI(GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               ):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description',]
    # permission_classes = (IsAuthenticated, )
