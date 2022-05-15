import requests
import os
from requests import auth
from requests.auth import HTTPBasicAuth
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()
consumer_key = os.getenv('CONSUMER_KEY')
secret_key = os.getenv('SECRET_KEY')

def generate_token():
    res = requests.get(settings.ACCESS_TOKEN_URL, auth=HTTPBasicAuth(consumer_key, secret_key))
    json_res = res.json()
    access_token = json_res['access_token']
    
    return access_token