from rest_framework import serializers
from salah.models import Depart , Products,Images


class Departserializer(serializers.ModelSerializer):
    class Meta:
        model = Depart
        fields = ('id','name')

class Productsserializer(serializers.ModelSerializer):
    depart = Departserializer()
    class Meta:
        model = Products
        fields = '__all__'

class Imagesserializer(serializers.ModelSerializer):
    products = Productsserializer()
    class Meta:
        model = Images
        fields = '__all__'
