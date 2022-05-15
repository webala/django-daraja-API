import requests
from django.shortcuts import render
from api.serializers import MakePaymentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.conf import settings
import json
from .access_token_encoding import generate_password
from .date_formating import format_date_time
from .generate_token import generate_token

# Create your views here.


class InitiateSTKPush(GenericAPIView):
    serializer_class = MakePaymentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        requestData = request.data
        amount = requestData.get('amount')
        phone = requestData.get('phone_number')