from django.urls import path
from . import views

app_name = 'service_provider'

urlpatterns = [
    path('provider/', views.index, name='index'),
    path('provider/analytics/', views.view_analytics, name='analytics'),
]
