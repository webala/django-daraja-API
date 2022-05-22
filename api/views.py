from urllib import response
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

        payment_response = self.initiate_mpesa_stk(amount, phone)
        print(payment_response)
        return Response(payment_response)

    def initiate_mpesa_stk(self, amount:str, phone:str) -> dict:
        access_token = generate_token()
        formated_time = format_date_time()
        password = generate_password(formated_time)

        headers ={
            'Authorization': 'Bearer %s' % access_token
        }

        payload = {    
            "BusinessShortCode":"174379",    
            "Password": password,    
            "Timestamp": formated_time,    
            "TransactionType": "CustomerPayBillOnline",    
            "Amount":amount,    
            "PartyA":phone,    
            "PartyB":"174379",    
            "PhoneNumber":phone,    
            "CallBackURL":"https://posthere.io/08b5-411f-8389",    
            "AccountReference":"ONLINE PAYMENT LIMITED",    
            "TransactionDesc":"Make Payment"
        }

        response = requests.post(
            settings.API_RESOURE_URL, headers=headers, json=payload
        )

        string_response = response.text
        string_object = json.loads(string_response)

        if 'errorCode' in string_object:
            print('Error: ', string_object)
            return string_object
        else:
            data = {
                'merchant_request_id' :string_object['MerchantRequestID'],
                'chechout_request_id' :string_object['CheckoutRequestID'],
                'response_code' :string_object['ResponseCode'],
                'response_description' :string_object['ResponseDescription'],
                'customer_meaasge' :string_object['CustomerMessage'],
            }
        
        return data