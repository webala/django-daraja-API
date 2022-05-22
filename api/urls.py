from django.urls import path, include
from .views import InitiateSTKPush

urlpatterns = [
    path('mpesa/', InitiateSTKPush.as_view(), name='lipa_na_mpesa')
]


