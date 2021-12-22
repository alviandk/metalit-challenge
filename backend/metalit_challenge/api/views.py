from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Challenge
from .serializers import ChallengeSerializer

# Create your views here.

class ChallengeView(APIView):
  def get(self, request):
    """
    GET all challenge already published
    """
    query = Challenge.objects.filter(status='published')
    serializers = ChallengeSerializer(query, many=True)
    return Response(serializers.data)

class ChallengeTaskView(APIView):
  pass

class TaskView(APIView):
  def get(self, request):
    """
    GET all task based on challenge ID
    """
    pass