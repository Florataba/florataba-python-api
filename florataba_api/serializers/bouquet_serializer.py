from rest_framework import serializers

from florataba_api.models.bouquet import Bouquet


class BouquetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bouquet
        fields = '__all__'
