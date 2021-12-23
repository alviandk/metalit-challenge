from django.shortcuts import get_list_or_404
from rest_framework import serializers, status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Challenge, Task, TaskVerification
from .serializers import ChallengeSerializer, TaskSerializer, TaskVerificationSerializer

# Create your views here.

"""TODO: custom pagination for each API (?), test API"""

### CHALLENGE AND TASK ###

class ChallengeView(ListAPIView):
  """
  GET all challenge already published
  """
  queryset = Challenge.objects.filter(status='published')
  serializer_class = ChallengeSerializer
  pagination_class = PageNumberPagination

class TaskView(ListAPIView):
  """
  GET all tasks by challenge id
  """
  serializer_class = TaskSerializer
  pagination_class = PageNumberPagination

  def get_queryset(self):
    """
    Override default queryset method on ListAPIView
    """
    query = Task.objects.filter(
      challenge_id = self.kwargs['challenge_id']
    ).order_by('id')
    obj = get_list_or_404(query)
    return obj

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
    if not challenge_query.exists() and not task_query.exists():
      return Response({"description": "challenge ID not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"challenge": challenge_serializers.data, "tasks": task_serializers.data})


### TASK VERIFICATION ###

class TaskVerificationView(ListCreateAPIView):
  """
  GET all data from task verification table
  """
  queryset = TaskVerification.objects.all().order_by('id')
  serializer_class = TaskVerificationSerializer
  pagination_class = PageNumberPagination

  def create(self, request, *args, **kwargs):
    """Override create method for creating new task verification item"""
    task_id = Task.objects.get(id=request.data['task'])
    task_id_serializer = TaskSerializer(task_id, many=False)
    task_challenge_id = task_id_serializer.data['challenge']

    serializer = TaskVerificationSerializer(data=request.data)

    if (request.data['challenge'] == task_challenge_id) and serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({"detail": "the task does not match with the challenge"})

class VerifiedTaskVerificationView(ListAPIView):
  """
  GET all verified task
  """
  queryset = TaskVerification.objects.filter(is_verified=True).order_by('id')
  serializer_class = TaskVerificationSerializer
  pagination_class = PageNumberPagination

class UnverifiedTaskVerificationView(ListAPIView):
  """
  GET all unverified task
  """
  queryset = TaskVerification.objects.filter(is_verified=False).order_by('id')
  serializer_class = TaskVerificationSerializer
  pagination_class = PageNumberPagination