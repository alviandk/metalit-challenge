from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.shortcuts import get_list_or_404
from rest_framework import status
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     ListCreateAPIView, RetrieveUpdateAPIView,)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsOwnerObjectPermission

from .auth import UserAuthentication

from .models import (Challenge, Task, TaskVerification, User, UserChallenge,
                     UserTask)
from .serializers import (ChallengeSerializer, TaskSerializer,
                          TaskVerificationSerializer, UserChallengeSerializer, UserSerializer,
                          UserTaskSerializer)

# JWT mockup import
from .auth import TokenHandler

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

  def list(self, request):
    queryset = self.get_queryset()
    serializer = ChallengeSerializer(queryset, many = True)

    page = self.paginate_queryset(queryset)
    if page is not None:
      serializer = self.get_serializer(page, many=True)

      # add total_reward attribute
      for i in range(len(serializer.data)):
        total_reward = 0
        challenge_id = serializer.data[i]['id']
        task_query = Task.objects.filter(challenge=challenge_id)
        for item in task_query:
          total_reward += item.reward_amount
        serializer.data[i]['total_reward'] = total_reward

      return self.get_paginated_response(serializer.data)

    serializer = self.get_serializer(queryset, many=True)

    # add total_reward attribute
    for i in range(len(serializer.data)):
      total_reward = 0
      challenge_id = serializer.data[i]['id']
      task_query = Task.objects.filter(challenge=challenge_id)
      for item in task_query:
        total_reward += item.reward_amount
      serializer.data[i]['total_reward'] = total_reward

    return Response(serializer.data)

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
    )
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
  queryset = TaskVerification.objects.all()
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
  queryset = TaskVerification.objects.filter(is_verified=True)
  serializer_class = TaskVerificationSerializer
  pagination_class = PageNumberPagination

class UnverifiedTaskVerificationView(ListAPIView):
  """
  GET all unverified task
  """
  queryset = TaskVerification.objects.filter(is_verified=False)
  serializer_class = TaskVerificationSerializer
  pagination_class = PageNumberPagination

### USER CHALLENGE ###

class UserChallengeIndividualView(RetrieveUpdateAPIView):
  """
  GET and PATCH invidual data from user challenge table by user id and challenge id
  """
  authentication_classes = [UserAuthentication]
  permission_classes = [IsOwnerObjectPermission]

  serializer_class = UserChallengeSerializer
  pagination_class = PageNumberPagination
  lookup_field = 'challenge_id'

  def get_queryset(self):
    uid = self.request.user[0].id
    queryset = UserChallenge.objects.filter(user_id=uid)
    return queryset

class UserChallengeListView(ListAPIView):
  """
  GET all challenge by user id
  """
  authentication_classes = [UserAuthentication]

  # queryset = UserChallenge.objects.all()
  serializer_class = UserChallengeSerializer
  pagination_class = PageNumberPagination
  # lookup_field = 'user_id'

  def get_queryset(self):
    """"
    Override default queryset method on ListAPIView
    """

    # Get uid from authentication method
    uid = self.request.user[0].id

    query = UserChallenge.objects.filter(
      user_id = uid
    )

    # Check if challenge exist

    obj = get_list_or_404(query)
    return obj

class CreateUserChallengeView(CreateAPIView):
  """
  POST data to user challenge table
  """
  authentication_classes = [UserAuthentication]

  queryset = UserChallenge.objects.all()
  serializer_class = UserChallengeSerializer

  def create(self, request, *args, **kwargs):
    """
    Override create method to validate that only published challenge are allowed to be enrolled
    """
    try:
      data_serializer = self.get_serializer(data=request.data)

      #check if request body contains invalid input
      if data_serializer.is_valid(raise_exception=True):
        challenge = Challenge.objects.get(id=data_serializer.validated_data.get('challenge').id)
        if challenge.status == 'published':
          self.perform_create(data_serializer)
          headers = self.get_success_headers(data_serializer.data)
          return Response(data_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
          return Response({"detail": "challenge is not published"}, status=status.HTTP_400_BAD_REQUEST)

    except IntegrityError:
      return Response({"detail": "user already enrolled in the challenge"}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
      return Response({"detail": "challenge enrollment failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

### USER TASK ###

class UserTaskListView(ListAPIView):
  """
  GET all task by challenge id and user id
  """
  authentication_classes = [UserAuthentication]

  serializer_class = UserTaskSerializer
  pagination_class = PageNumberPagination

  def get_queryset(self):
    """
    Override default queryset method on ListAPIView
    """

    # Get uid from authentication method
    uid = self.request.user[0].id

    query = UserTask.objects.filter(
      user_id = uid,
      task__challenge__id = self.kwargs['challenge_id']
    )

    #Check if task in the challenge

    obj = get_list_or_404(query)
    return obj

class UserTaskListCompletedView(ListAPIView):
  """
  GET all completed task by challenge id and user id
  """
  authentication_classes = [UserAuthentication]

  serializer_class = UserTaskSerializer
  pagination_class = PageNumberPagination

  def get_queryset(self):
    """
    Override default queryset method on ListAPIView
    """

    # Get uid from authentication method
    uid = self.request.user[0].id

    query = UserTask.objects.filter(
      user_id = uid,
      status = 'completed',
      task__challenge__id = self.kwargs['challenge_id']
    )

    #Check if task in the challenge

    obj = get_list_or_404(query)
    return obj

class UserTaskListUncompletedView(ListAPIView):
  """
  GET all uncompleted tak by challenge id and user id
  """
  authentication_classes = [UserAuthentication]

  serializer_class = UserTaskSerializer
  pagination_class = PageNumberPagination

  def get_queryset(self):
    """
    Override default queryset method on ListAPIView
    """

    # Get uid from authentication method
    uid = self.request.user[0].id

    query = UserTask.objects.filter(
      user_id = uid,
      status = 'uncompleted',
      task__challenge__id = self.kwargs['challenge_id']
    )

    #Check if task in the challenge

    obj = get_list_or_404(query)
    return obj

class CreateUserTaskView(CreateAPIView):
  """
  POST data to user task table
  """    
  authentication_classes = [UserAuthentication]

  queryset = UserTask.objects.all()
  serializer_class = UserTaskSerializer

  def create(self, request, *args, **kwargs):
    try:
      data_serializer = self.get_serializer(data=request.data)

      #check if request body contains invalid input
      if data_serializer.is_valid(raise_exception=True):

        task = Task.objects.get(id=data_serializer.validated_data.get('task').id)
        challenge_id = task.challenge.id

        # check if user already enrolled in the challenge (if not raise an exception)
        query = UserChallenge.objects.get(challenge=challenge_id, user=data_serializer.validated_data.get('user').id)

        self.perform_create(data_serializer)
        headers = self.get_success_headers(data_serializer.data)
        return Response(data_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    except ObjectDoesNotExist:
      return Response({"detail": "user not enrolled in the challenge/task does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
    except IntegrityError:
      return Response({"detail": "user already enrolled in the task"}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
      return Response({"detail": "task enrollment failed"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GenerateJWTMockup(APIView):
  """
  Mockup API to generate JWT token
  """
  def get(self, request, *args, **kwargs):
    # Mockup query
    query = User.objects.get(id=kwargs.get('user_id'))
    serializer = UserSerializer(query, many=False)

    # JWT encode process
    encoded_data, token = TokenHandler.token_encode(serializer.data, 24)

    return Response({"data_from_query": encoded_data, "token": token}, status=status.HTTP_200_OK)

class TestJWTResponse(APIView):
  """
  Mockup API to test JWT token generated
  """
  authentication_classes = [UserAuthentication]
  def get(self, request):
    # if authorization header is specified and jwt token is valid
    return Response({"message": "testing JWT success"})

### User Challenge Task
class CustomPagination(PageNumberPagination):
  page_size_query_param = 'page'


class UserChallengeTaskView(APIView):
  """
  GET challenge and all of it's task based on uid and challenge id
  """
  # TODO: pagination
  pagination_class = CustomPagination
  
  def get(self, request, *args, **kwargs):
    # Get challenge
    challenge_query = UserChallenge.objects.get(challenge_id=kwargs.get('challenge_id'), user_id=kwargs.get('user_id'))
    challenge_serializer = UserChallengeSerializer(challenge_query)

    #Get task
    task_query = UserTask.objects.filter(task__challenge__id = self.kwargs['challenge_id'], user_id=kwargs.get('user_id'))
    task_serializer = UserTaskSerializer(task_query, many=True)

    return Response({
      "challenge": challenge_serializer.data,
      "tasks": task_serializer.data
    }, status=status.HTTP_200_OK)