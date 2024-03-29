import logging

from django.core.validators import (
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
)
from django.forms import ValidationError
from products.models import Order
from rest_framework import serializers

from .models import Payment

log = logging.getLogger(__name__)


class PlasticCardSerializer(serializers.Serializer):
    number = serializers.IntegerField(
        required=True,
        validators=[MinValueValidator(1), MaxValueValidator(99_999_999)],
    )
    name = serializers.CharField(
        required=True, max_length=255, validators=[MinLengthValidator(1)]
    )
    month = serializers.CharField(
        required=True, max_length=2, validators=[MinLengthValidator(2)]
    )
    year = serializers.IntegerField(
        required=True,
        validators=[MinValueValidator(1000), MaxValueValidator(9999)],
    )
    code = serializers.IntegerField(
        required=True,
        validators=[MinValueValidator(100), MaxValueValidator(999)],
    )

    def validate_month(self, value):
        try:
            int_value = int(value)
        except ValueError:
            raise ValidationError('Ensure this value is an integer')

        if not 1 <= int_value <= 12:
            raise ValidationError(
                'Ensure this value is a two-digit value from 01 to 12'
            )

        return value


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order_id', 'number', 'name', 'paid_sum']

    order_id = serializers.IntegerField(
        required=True,
        write_only=True,
        validators=[MinValueValidator(1)],
    )
    number = serializers.IntegerField(
        required=True,
        write_only=True,
        source='card_number',
        validators=[MinValueValidator(1), MaxValueValidator(99_999_999)],
    )
    name = serializers.CharField(
        required=True,
        write_only=True,
        max_length=255,
        validators=[MinLengthValidator(1)],
    )
    paid_sum = serializers.DecimalField(
        required=True,
        write_only=True,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    def create(self, validated_data):
        order = Order.objects.filter(
            id=validated_data['order_id'], archived=False
        ).first()
        if order is None:
            raise ValidationError({'order_id': 'Order does not exist'})
        payment = Payment.objects.create(**validated_data)

        return payment
