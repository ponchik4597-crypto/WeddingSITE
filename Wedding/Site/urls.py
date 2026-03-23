from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='weddingsite'),
    path('location/', location, name='location'),
    path('presence/', presence, name='presence'),
    path('dress_code/', dress_code, name='dress_code'),
    path('thank_you/', thank_you, name='thank_you'),
]
