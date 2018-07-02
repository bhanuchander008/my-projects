from rest_framework import serializers
from .models import SquareTest
class SquareTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SquareTest
        fields = ('Number','SquareNumber')
