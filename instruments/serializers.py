from rest_framework import serializers
from .models import Instrument, Order
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    def validate_username(self, value):
        existing_users = User.objects.filter(username=value)
        if self.instance:
            existing_users = existing_users.exclude(pk=self.instance.pk)

        if existing_users.exists():
            raise serializers.ValidationError("Це ім'я користувача вже зайнято.")
        return value

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

