from django.urls import path, include
from .views import (
    website_home, 
)

urlpatterns = [
    path('', website_home, name='website_home'), 
]