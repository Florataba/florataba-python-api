from rest_framework import serializers

from domain.models.orders import Bouquet


class BouquetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bouquet
        fields = '__all__'
