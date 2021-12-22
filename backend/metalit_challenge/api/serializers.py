from django.db.models import fields
from rest_framework import serializers
from .models import Challenge, Task, TaskVerification

class ChallengeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Challenge
    fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'

class TaskVerificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = TaskVerification
    fields = '__all__'