from rest_framework import serializers
from .models import*
class TumanSerializers(serializers.ModelSerializer):
    class Meta:
        model=Tumanlar
        fields = ['id','name']

class UySerializers(serializers.ModelSerializer):
    tumanda=TumanSerializers(many=False, read_only=True)
    class Meta:
        model=Uylar
        fields = ['id', 'xona_soni', 'narx','tumanda','manzil','qoshimchajxozlar']
