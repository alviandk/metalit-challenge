from django.urls import reverse
import json
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Challenge
from api.serializers import ChallengeSerializer


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