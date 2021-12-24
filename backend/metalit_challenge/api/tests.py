from datetime import datetime
from django.test import TestCase, RequestFactory
from django.urls import reverse
import json
from rest_framework import serializers, status
from rest_framework.test import APIRequestFactory, APITestCase

from .models import Challenge, Task, TaskVerification
from .serializers import ChallengeSerializer, TaskSerializer, TaskVerificationSerializer

# Create your tests here.

class ChallengeTestCase(APITestCase):
  def setUp(self):
    """
    Setup before the test run
    """
    self.register_url =  reverse('challenge')
    Challenge.objects.create(name="test_challenge",
                             description="test_description",
                             status="published",
                             budget="5000",)

  def test_get_challenge(self):
    """
    Test to make sure that the challenge API will work and return status code 200
    """
    query = Challenge.objects.all()
    serializer = ChallengeSerializer(query, many = True)

    response = self.client.get(self.register_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.dumps(response.json()['results']), json.dumps(serializer.data))
  
  def test_post_challenge(self):
    """
    Test to make sure that the challenge API will not work and return status code 405
    """
    response = self.client.post(self.register_url)
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
  
  def test_put_challenge(self):
    """
    Test to make sure that the challenge API will not work and return status code 405
    """
    response = self.client.put(self.register_url)
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class TaskTestCase(APITestCase):
  def setUp(self):
    """
    Setup before the test run
    """
    pass
    # self.register_url = reverse('task', kwargs={'challenge_id':1})
    # Challenge.objects.create(name="test_challenge1",
    #                          description="test_description1",
    #                          status="unpublished1",
    #                          budget=50000,)
    # Task.objects.create(challenge_id=2,
    #                     name="task-test1",
    #                     description="description1",
    #                     reward_amount=50000,)

# class TaskVerificationTestCase(TestCase):
#   def setUp(self):
#     Challenge.objects.create(name="test_challenge",
#                              description="test_description",
#                              status="unpublished",
#                              budget=50000,)
#     Task.objects.create(challenge_id=1,
#                         name="task-test",
#                         description="description",
#                         reward_amount=50000,)

#   def test_create_task_verification(self):
#     """
#     Test to make sure that the task verification API will create task verification
#     """
#     query = Challenge.objects.all()
#     serializer = ChallengeSerializer(query, many = True)
#     print(json.dumps(serializer.data))
#     # data = {
#     #   "submission": "www.example.com",
#     #   "challenge": 1,
#     #   "task": 2
#     # }
#     # response = self.client.post('/api/task-verification', data)
#     # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

