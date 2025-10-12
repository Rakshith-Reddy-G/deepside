from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('Register1/', views.Register1, name='Register1'),
    path('ViewYourProfile/', views.ViewYourProfile, name='ViewYourProfile'),
    path('Predict_Drug_Side_Effect_Type/', views.Predict_Drug_Side_Effect_Type, name='Predict_Drug_Side_Effect_Type'),
    path('prediction_history/', views.prediction_history, name='prediction_history'),
    path('logout/', views.logout, name='logout'),
]
