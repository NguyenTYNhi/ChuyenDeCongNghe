from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

def even_number(value):
    if value % 2 != 0:
        raise serializers.ValidationError("This field must be an even number.")

class MultipleOf:
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if value % self.base != 0:
            raise serializers.ValidationError(f"This field must be a multiple of {self.base}.")

class DemoSerializer(serializers.Serializer):
    number = serializers.IntegerField(validators=[even_number, MultipleOf(5)])
    slug = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=[])]
    )

class DemoTogetherSerializer(serializers.Serializer):
    field1 = serializers.CharField()
    field2 = serializers.CharField()

    class Meta:
        validators = [
            UniqueTogetherValidator(queryset=[], fields=['field1', 'field2'])
        ]
