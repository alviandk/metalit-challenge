from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Challenge, Task
from .serializers import ChallengeSerializer, TaskSerializer

# Create your views here.

class ChallengeView(APIView):
  def get(self, request):
    """
    GET all challenge already published
    """
    query = Challenge.objects.filter(status='published')
    serializers = ChallengeSerializer(query, many=True)
    return Response(serializers.data)

class TaskView(APIView):
  """
  GET all tasks by challenge id
  """
  def get_task(self, challenge_id):
    return Task.objects.filter(challenge_id=challenge_id)

  def get(self, request, challenge_id):
    query = self.get_task(challenge_id)
    serializers = TaskSerializer(query, many=True)
    if query.count() != 0:
      return Response(serializers.data)
    else:
      return Response({"description": "challenge ID not found"}, status=status.HTTP_404_NOT_FOUND)

class ChallengeTaskView(APIView):
  """
  GET challenge and all of it's tasks
  """
  def get_challenge(self, challenge_id):
    return Challenge.objects.filter(id=challenge_id)

  def get_task(self, challenge_id):
    return Task.objects.filter(challenge_id=challenge_id)

  def get(self, request, challenge_id):
    challenge_query = self.get_challenge(challenge_id)
    task_query = self.get_task(challenge_id)
    challenge_serializers = ChallengeSerializer(challenge_query, many=True)
    task_serializers = TaskSerializer(task_query, many=True)
    if challenge_query.count() == 0 and task_query.count() == 0:
      return Response({"description": "challenge ID not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"challenge": challenge_serializers.data, "tasks": task_serializers.data})