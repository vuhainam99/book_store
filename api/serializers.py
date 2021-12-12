from .models import *

from rest_framework import serializers





class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"



# class TcsTransportOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TcsTransportOrder
#         fields = "__all__"