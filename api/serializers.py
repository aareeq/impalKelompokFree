from rest_framework import serializers
from .models import Anggota, Buku, Transaksi
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        # hash user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user
    
class AnggotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anggota
        fields = '__all__'

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'

class TransaksiSerializer(serializers.ModelSerializer):
    buku = BukuSerializer(read_only=True)
    anggota = AnggotaSerializer(read_only=True)

    class Meta:
        model = Transaksi
        fields = '__all__'