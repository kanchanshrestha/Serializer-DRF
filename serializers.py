from rest_framework import serializers
class Studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=25)
    roll_no=serializers.IntegerField()
    country=serializers.CharField(max_length=25)

