from rest_framework.generics import ListAPIView, CreateAPIView

from apps.settings.models import Settings
from apps.settings.serializers import SettingsSerializer

# Create your views here.
class SettingsApi(ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer


