from django.urls import reverse
import json
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, RequestsClient

from api.models import Challenge, User, UserChallenge
from api.serializers import UserChallengeSerializer

class UserChallengeTestCase(APITestCase):
  def setUp(self):
    """
    Setup before the test run
    """
    self.user_challenge_url =  reverse('user-challenge-all')
    self.challenge = Challenge.objects.create(name="test_challenge",
                                            description="test_description",
                                            status="published",
                                            budget="5000",)
    self.user = User.objects.create(name="user-test")
    self.user_challenge = UserChallenge.objects.create(challenge=self.challenge,
                                user=self.user,)
    self.auth_url = reverse('generate-token', kwargs={'user_id':self.user.id})
    

  def test_get_user_challenge_auth_success(self):
    """
    Test to make sure that user challenge API will work and return status code 200 if authentication succeeded
    """
    # Get data from db
    query = UserChallenge.objects.all()
    user = User.objects.get(name="user-test")
    serializer = UserChallengeSerializer(query, many = True)

    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}
    request = self.client.get(self.user_challenge_url, **header)

    # Test
    self.assertEqual(request.status_code, status.HTTP_200_OK)
    self.assertEqual(json.dumps(request.json()['results']), json.dumps(serializer.data))

  def test_get_user_challenge_auth_fail_no_header(self):
    """
    Test to make sure that user challenge API will not work if no Authorization header is provided
    """
    # Simulate fail authentication
    request = self.client.get(self.user_challenge_url)

    self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)
  
  def test_get_user_challenge_auth_fail_jwt_expired_or_invalid(self):
    """
    Test to make sure that user challenge API will not work if JWT token provided in Authorization header is invalid/expired
    """
    # Simulate fail authentication
    header = {'HTTP_AUTHORIZATION': 'Token invalidtoken'}
    request = self.client.get(self.user_challenge_url, **header)

    self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

  def test_post_user_challenge(self):
    """
    Test to make sure that user challenge API will not work with POST method and return status code 405 if authenticated
    """
    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}

    request = self.client.post(self.user_challenge_url, **header)

    self.assertEqual(request.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
  
  def test_put_user_challenge(self):
    """
    Test to make sure that user challenge API will not work with PUT method and return status code 405 if authenticated
    """
    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}

    request = self.client.put(self.user_challenge_url, **header)

    self.assertEqual(request.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class UserChallengeIndividualTestCase(APITestCase):
  def setUp(self):
    """
    Setup before the test run
    """
    self.challenge = Challenge.objects.create(name="test_challenge",
                                            description="test_description",
                                            status="published",
                                            budget="5000",)
    self.user = User.objects.create(name="user-test")
    self.user_challenge = UserChallenge.objects.create(challenge=self.challenge,
                                user=self.user,)
    self.user_challenge_url =  reverse('user-challenge-individual', kwargs={'challenge_id':self.challenge.id})
    self.auth_url = reverse('generate-token', kwargs={'user_id':self.user.id})

  def test_get_user_challenge_auth_success(self):
    """
    Test to make sure that user challenge API will work and return status code 200 if authentication succeeded
    """
    # Get data from db
    query = UserChallenge.objects.filter(user_id=self.user.id, challenge_id=self.challenge.id)
    serializer = UserChallengeSerializer(query, many = True)
    
    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}
    request = self.client.get(self.user_challenge_url, **header)

    # Test
    self.assertEqual(request.status_code, status.HTTP_200_OK)
    self.assertEqual(json.dumps(request.json()), json.dumps(serializer.data[0]))

  def test_get_user_challenge_individual_auth_fail_no_header(self):
    """
    Test to make sure that user challenge individual API will not work if no Authorization header is provided
    """
    # Simulate fail authentication
    request = self.client.get(self.user_challenge_url)

    self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)
  
  def test_get_user_challenge_auth_fail_jwt_expired_or_invalid(self):
    """
    Test to make sure that user challenge individual API will not work if JWT token provided in Authorization header is invalid/expired
    """
    # Simulate fail authentication
    header = {'HTTP_AUTHORIZATION': 'Token invalidtoken'}
    request = self.client.get(self.user_challenge_url, **header)

    self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

  def test_post_user_individual_challenge(self):
    """
    Test to make sure that user challenge individual API will not work with POST method and return status code 405 if authenticated
    """
    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}

    request = self.client.post(self.user_challenge_url, **header)

    self.assertEqual(request.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
  
  def test_patch_user_challenge_individual_auth_fail_no_header(self):
    """
    Test to make sure that user challenge individual API will not work with PATCH method if no Authorization header is provided
    """
    # Simulate fail authentication
    request = self.client.patch(self.user_challenge_url)

    self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

  def test_patch_user_challenge_individual_jwt_expired_or_invalid(self):
    """
    Test to make sure that user challenge individual API will not work with PATCH method if JWT token provided in Authorization header is invalid/expired
    """
    # Simulate fail authentication
    header = {'HTTP_AUTHORIZATION': 'Token invalidtoken'}
    request = self.client.patch(self.user_challenge_url, **header)

    self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)
  
  def test_patch_user_challenge_individual(self):
    """
    Test to make sure that user challenge individual API will work with PATCH method if authenticated
    """
    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}

    data = {
      "status": "completed"
    }

    request = self.client.patch(self.user_challenge_url, data, **header)

    # Get data from db
    query = UserChallenge.objects.filter(user_id=self.user.id, challenge_id=self.challenge.id)
    serializer = UserChallengeSerializer(query, many = True)
    serializer.data[0]['status'] = "completed"
    
    self.assertEqual(request.status_code, status.HTTP_200_OK)
    self.assertEqual(request.data, serializer.data[0])

class UserChallengeCreationTestCase(APITestCase):
  def setUp(self):
    """
    Setup before the test run
    """
    self.user_challenge_url =  reverse('user-challenge-creation')
    self.challenge = Challenge.objects.create(name="test_challenge",
                                            description="test_description",
                                            status="published",
                                            budget="5000",)
    self.user = User.objects.create(name="user-test")
    self.auth_url = reverse('generate-token', kwargs={'user_id':self.user.id})
  
  def test_post_user_challenge_creation_auth_fail_no_header(self):
    """
    Test to make sure that user challenge creation API will not work with POST method if no Authorization header is provided
    """
    # Simulate fail authentication
    request = self.client.patch(self.user_challenge_url)

    self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

  def test_post_user_challenge_individual_jwt_expired_or_invalid(self):
    """
    Test to make sure that user challenge creation API will not work with POST method if JWT token provided in Authorization header is invalid/expired
    """
    # Simulate fail authentication
    header = {'HTTP_AUTHORIZATION': 'Token invalidtoken'}
    request = self.client.patch(self.user_challenge_url, **header)

    self.assertEqual(request.status_code, status.HTTP_403_FORBIDDEN)

  def test_post_user_challenge_individual(self):
    """
    Test to make sure that user challenge creation API will work with POST method if authenticated
    """
    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}

    data = {
      "user": self.user.id,
      "challenge": self.challenge.id
    }

    request = self.client.post(self.user_challenge_url, data, **header)
    self.assertEqual(request.status_code, status.HTTP_201_CREATED)
  
  def test_get_user_challenge_creation(self):
    """
    Test to make sure that user challenge creation API will not work with GET method and return status code 405 if authenticated
    """
    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}

    request = self.client.get(self.user_challenge_url, **header)
    
    self.assertEqual(request.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

  def test_put_user_challenge_creation(self):
    """
    Test to make sure that user challenge creation API will not work with PUT method and return status code 405 if authenticated
    """
    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']

    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}

    request = self.client.put(self.user_challenge_url, **header)
    
    self.assertEqual(request.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

  def test_patch_user_challenge_createion(self):
    """
    Test to make sure that user challenge creation API will not work with PATCH method and return status code 405 if authenticated
    """
    # Simulate successful authentication
    auth_request = self.client.get(self.auth_url)
    jwt_token = auth_request.data['token']
    
    header = {'HTTP_AUTHORIZATION': f'Token {jwt_token}'}

    request = self.client.get(self.user_challenge_url, **header)
    
    self.assertEqual(request.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)