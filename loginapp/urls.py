from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.custom_logout, name='logout'),
]
