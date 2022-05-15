from rest_framework import serializers

class MakePaymentSerializer (serializers.Serializer):
    amount = serializers.CharField()
    phone_number = serializers.CharField()