from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='weddingsite'),
    path('details/', details, name='details'),
    path('presence/', presence, name='presence'),
    path('thank_you/', thank_you, name='thank_you'),
    path('not_coming/', not_coming, name='not_coming'),
]
