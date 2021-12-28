from django.db.models import fields
from rest_framework import serializers
from .models import Challenge, Task, TaskVerification, UserChallenge, UserTask

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

class UserTaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserTask
    fields = '__all__'

class UserChallengeSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserChallenge
    fields = '__all__'