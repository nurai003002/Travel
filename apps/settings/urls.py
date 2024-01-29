from django.urls import path


from apps.settings.views import SettingsApi

urlpatterns = [
    path('', SettingsApi.as_view(), name='api_settings')
    
]