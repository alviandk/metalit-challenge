from datetime import datetime
from django.test import TestCase, RequestFactory
from django.urls import reverse
import json
from rest_framework import serializers, status
from rest_framework.test import APIRequestFactory, APITestCase

from api.models import Challenge, Task, TaskVerification
from api.serializers import ChallengeSerializer, TaskSerializer, TaskVerificationSerializer


class TaskVerificationTestCase(TestCase):
  def setUp(self):
    """
    Setup before the test run
    """
    self.challenge = Challenge.objects.create(name="test_challenge",
                             description="test_description",
                             status="unpublished",
                             budget=50000,)
    Task.objects.create(challenge=self.challenge,
                        name="task-test",
                        description="description",
                        reward_amount=50000,)
    self.register_url = reverse('task_verification')

  # def test_post_task_verification(self):
  #   """
  #   Test to make sure that the task verification API will create task verification
  #   """
  #   query1 = Challenge.objects.get(id=1)
  #   serializer1 = ChallengeSerializer(query1, many = False)
  #   print(serializer1.data)
  #   query = Task.objects.get(challenge_id=1)
  #   serializer = TaskSerializer(query, many = False)
  #   print(serializer.data)
  #   data = {
  #     "submission": "www.example.com",
  #     "challenge": 1,
  #     "task": 1
  #   }   
  #   response = self.client.post('/api/task-verification', data)
  #   print(self.register_url)
  #   print(response.data)
  #   self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  # def test_post_task_verification_task_not_exist(self):
  #   """
  #   Test to make sure that the task verification API will not create task-verification data
  #   """
  #   data = {
  #     "submission": "www.example.com",
  #     "challenge": 1,
  #     "task": 99
  #   }   
  #   response = self.client.post('/api/task-verification', data)
  #   self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

