from django.urls import reverse
import json
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, RequestsClient

from api.models import Challenge, User, UserChallenge, UserTask, Task
from api.serializers import UserTaskSerializer

class UserTaskTestCase(APITestCase):
  def setUp(self):
    """
    Setup before the test run
    """
    self.challenge = Challenge.objects.create(name="test_challenge",
                                              description="test_description",
                                              status="published",
                                              budget=5000,)
    self.task = Task.objects.create(challenge=self.challenge,
                                    name="task-test",
                                    description="description",
                                    reward_amount=5000)
    self.user = User.objects.create(name="user-test")
    self.user_challenge = UserChallenge.objects.create(challenge=self.challenge,
                                                       user=self.user,)
    self.user_task = UserTask.objects.create(task=self.task,
                                             user=self.user,)
    self.user_task_url =  reverse('user-task-all', kwargs={'challenge_id':self.challenge.id})
    self.auth_url = reverse('generate-token', kwargs={'user_id':self.user.id})
    
  def test_get_user_task_auth_success(self):
    """
    Test to make sure that user task API will work and return status code 200 if authentication succeeded
    """
    # Get data from db
    query = UserTask.objects.all()
    user = User.objects.get(name="user-test")
    serializer = UserTaskSerializer(query, many = True)

    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}
    request = self.client.get(self.user_task_url, **header)

    # Test
    self.assertEqual(request.status_code, status.HTTP_200_OK)
    self.assertEqual(json.dumps(request.json()['results']), json.dumps(serializer.data))

  def test_get_user_challenge_auth_fail_no_header(self):
    """
    Test to make sure that user task API will not work if no Authorization header is provided
    """
    # Simulate fail authentication
    request = self.client.get(self.user_task_url)

    self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)
  
  def test_get_user_challenge_auth_fail_jwt_expired_or_invalid(self):
    """
    Test to make sure that user task API will not work if JWT token provided in Authorization header is invalid/expired
    """
    # Simulate fail authentication
    header = {'HTTP_AUTHORIZATION': 'Token invalidtoken'}
    request = self.client.get(self.user_task_url, **header)

    self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

  def test_post_user_challenge(self):
    """
    Test to make sure that user task API will not work with POST method and return status code 405 if authenticated
    """
    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}

    request = self.client.post(self.user_task_url, **header)

    self.assertEqual(request.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
  
  def test_put_user_challenge(self):
    """
    Test to make sure that user task API will not work with PUT method and return status code 405 if authenticated
    """
    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}

    request = self.client.put(self.user_task_url, **header)

    self.assertEqual(request.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
