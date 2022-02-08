from django.db.models import fields
from rest_framework import serializers

from .models import Challenge, Task, TaskVerification, User, UserChallenge, UserTask


class ChallengeSerializer(serializers.ModelSerializer):
    total_reward = serializers.IntegerField(source="sum_rewards")

    class Meta:
        model = Challenge
        fields = [
            "id",
            "name",
            "description",
            "status",
            "budget",
            "created_at",
            "end_date",
            "total_reward",
        ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskVerification
        fields = "__all__"


class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTask
        fields = "__all__"


class UserChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChallenge
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
