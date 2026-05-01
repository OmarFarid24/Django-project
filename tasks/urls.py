from django.urls import path
from .views import dashboard

urlpatterns = [
    path('lists/', dashboard, name='dashboard'),
]