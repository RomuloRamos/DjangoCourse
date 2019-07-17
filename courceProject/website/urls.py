from django.urls import path, include
from .views import (
    website_home, 
    website_contatos,
)

urlpatterns = [
    path('', website_home, name='website_home'), 
    path('contatos', website_contatos, name='website_contatos'),
    ]