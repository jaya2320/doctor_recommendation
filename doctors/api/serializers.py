from rest_framework import serializers, status

class DoctorSerializer(serializers.Serializer):
    disease = serializers.CharField(max_length=200)
    