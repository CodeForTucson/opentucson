from crime.models import Crime

from rest_framework import serializers


class CrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crime


class CrimeSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Crime
        fields = ('id', 'xcoord', 'ycoord', 'inci_id', 'start_date')
