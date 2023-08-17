from . import models
from rest_framework import serializers

def character_lower_limit(value):
    if value < 5:
        raise serializers.ValidationError('Value is less than 5')


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[character_lower_limit])   
    
    # def validate_name(self, value):
    #     if value[0]!='s':
    #         raise serializers.ValidationError('value shold start with s')
    
    # def validate(self,data):
    #     print(data)
    #     return data
    
    class Meta:
        model = models.Student
        fields = '__all__'
    
    # def create(self,validated_data):
    #     return models.Student.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.roll = validated_data.get('roll', instance.roll)
    #     instance.save()
    #     return instance
    

