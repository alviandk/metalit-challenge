from django.db.models import fields
from rest_framework import serializers
from .models import Challenge, Task

class ChallengeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Challenge
    fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    field = '__all__'