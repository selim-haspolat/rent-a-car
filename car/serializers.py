from rest_framework import serializers
from .models import (
    Car,
    Reservation
)

# -----------------------------------------
# FixSerializer
# -----------------------------------------
class FixSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False, read_only=True)
    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)



# -----------------------------------------
# CarSerializer
# -----------------------------------------
class CarSerializer(FixSerializer):
    
    class Meta:
        model = Car
        exclude = []
    
    def get_fields(self):
        fields = super().get_fields()
        user = self.context.get('request').user
        # STAFF değilse gösterilmeyecek fields:
        if not user.is_staff:
            fields.pop('created')
            fields.pop('updated')
            fields.pop('plate')
            fields.pop('availability')
            
        return fields


# -----------------------------------------
# ReservationSerializer
# -----------------------------------------
class ReservationSerializer(FixSerializer):
    car = serializers.StringRelatedField()
    car_id = serializers.IntegerField()

    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        exclude = []

    def get_total_price(self, obj):
        return obj.car.rent_per_day * (obj.end_date - obj.start_date).days