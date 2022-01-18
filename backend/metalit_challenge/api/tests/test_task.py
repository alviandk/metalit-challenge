from django.urls import reverse
import json
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Challenge, Task
from api.serializers import TaskSerializer


class TaskTestCase(APITestCase):
  def setUp(self):
    """
    Setup before the test run
    """
    self.challenge = Challenge.objects.create(name="test_challenge2",
                             description="test_description2",
                             status="published",
                             budget=50000,)
    self.task = Task.objects.create(challenge=self.challenge,
                       name="task-test",
                       description="description",
                       reward_amount=5000)
    self.register_url = reverse('task', kwargs={'challenge_id':1})

  def test_get_challenge(self):
    """
    Test to make sure that the task API will work and return status code 200
    """
    query = Task.objects.get(challenge_id=1)
    serializer = TaskSerializer(query, many = False)

    response = self.client.get(self.register_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(json.dumps(response.json()['results'][0]), json.dumps(serializer.data))
    print("Test GET completed")
  
  def test_post_challenge(self):
    """
    Test to make sure that the task API will not work and return status code 405
    """
    response = self.client.post(self.register_url)
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    print("Test POST completed")
  
  def test_put_challenge(self):
    """
    Test to make sure that the task API will not work and return status code 405
    """
    response = self.client.put(self.register_url)
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    print("Test PUT completed")


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

