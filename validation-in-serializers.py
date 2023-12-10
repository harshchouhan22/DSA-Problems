

from rest_framework import serializers
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)

class MyModelSerializer(serializers.ModelSerializer):
    name  = serializers.CharField(max_length = 100)
    age = serializers.IntegerField()
    def validate_age(self, value):
        "Validate that the age is not negative"
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        return value
    def validate(self, data):
        "validate entire data"
        name = data.get('name', '')
        if len(name) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return data
    
    class Meta:
        model = MyModel
        fields = '__all__'


# To Test This Serializer here in this py file
if __name__ == "__main__":
    #valid data
    valid_data ={'name': 'Jhon Doe', 'age': 25}

    #Invalid data
    invalid_data = {'name': 'Jane Doe', 'age': -45}

    #create serializers instances
    serializer_valid = MyModelSerializer(data = valid_data)
    serializer_invalid = MyModelSerializer(data=invalid_data)

    print("Valid Data: ")
    if serializer_valid.is_valid():
        validated_data = serializer_valid.validated_data
        print(f"Validated Data: {validated_data}")
    else:
        errors = serializer_valid.errors
        print(f"Errors: {errors}")

    print("Invalid Data: ")
    if serializer_invalid.is_valid():
        validate_data = serializer_invalid.validated_data
        print(f"Validated Data : {validated_data}")
    else:
        errors = serializer_invalid.errors
        print(f"Errors: {errors}")


