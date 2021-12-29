from django.http import Http404
from django.shortcuts import get_list_or_404
from rest_framework import mixins, pagination, serializers, status
from rest_framework.generics import (GenericAPIView, ListAPIView,
                                     ListCreateAPIView, RetrieveUpdateAPIView,
                                     UpdateAPIView)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .auth import UserAuthentication

from .models import (Challenge, Task, TaskVerification, User, UserChallenge,
                     UserTask)
from .serializers import (ChallengeSerializer, TaskSerializer,
                          TaskVerificationSerializer, UserChallengeSerializer, UserSerializer,
                          UserTaskSerializer)

# JWT mockup import
import jwt
from environs import Env

env = Env()
env.read_env()

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
  GET and POST all data from task verification table
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

### USER CHALLENGE ###

class UserChallengeIndividualView(RetrieveUpdateAPIView):
  """
  GET and PATCH invidual data from user challenge table by user id and challenge id
  """
  serializer_class = UserChallengeSerializer
  pagination_class = PageNumberPagination
  lookup_field = 'user_id'

  def get_queryset(self):
    challenge_id = self.request.query_params.get('challenge')
    queryset = UserChallenge.objects.filter(challenge_id=challenge_id)
    return queryset

class UserChallengeListView(ListAPIView):
  """
  GET all challenge by user id
  """
  queryset = UserChallenge.objects.all()
  serializer_class = UserChallengeSerializer
  pagination_class = PageNumberPagination
  lookup_field = 'user_id'

### USER TASK ###

class UserTaskListView(ListAPIView):
  """
  GET all task by challenge id and user id
  """
  serializer_class = UserTaskSerializer
  pagination_class = PageNumberPagination

  def get_queryset(self):
    """
    Override default queryset method on ListAPIView
    """
    query = UserTask.objects.filter(
      user_id = self.kwargs['user_id'],
      task__challenge__id = self.kwargs['challenge_id']
    ).order_by('id')

    #Check if task in the challenge

    obj = get_list_or_404(query)
    return obj

class UserTaskListCompletedView(ListAPIView):
  """
  GET all completed task by challenge id and user id
  """
  serializer_class = UserTaskSerializer
  pagination_class = PageNumberPagination

  def get_queryset(self):
    """
    Override default queryset method on ListAPIView
    """
    query = UserTask.objects.filter(
      user_id = self.kwargs['user_id'],
      status = 'completed',
      task__challenge__id = self.kwargs['challenge_id']
    ).order_by('id')

    #Check if task in the challenge

    obj = get_list_or_404(query)
    return obj

class UserTaskListUncompletedView(ListAPIView):
  """
  GET all uncompleted tak by challenge id and user id
  """
  serializer_class = UserTaskSerializer
  pagination_class = PageNumberPagination

  def get_queryset(self):
    """
    Override default queryset method on ListAPIView
    """
    query = UserTask.objects.filter(
      user_id = self.kwargs['user_id'],
      status = 'uncompleted',
      task__challenge__id = self.kwargs['challenge_id']
    ).order_by('id')

    #Check if task in the challenge

    obj = get_list_or_404(query)
    return obj

class GenerateJWTMockup(APIView):
  """
  Mockup API to generate JWT token
  """
  authentication_classes = (UserAuthentication,)
  def get(self, request):
    # Mockup query
    query = User.objects.get(id=1)
    serializer = UserSerializer(query, many=False)
    # JWT encode process
    key = env('JWT_SECRET_KEY')
    token = jwt.encode(serializer.data, key, algorithm="HS256")

    return Response({"data_from_query": serializer.data, "token": token}, status=status.HTTP_200_OK)