from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Contact
		fields = '__all__'
  