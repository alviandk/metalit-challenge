from django.contrib import auth
import jwt
from environs import Env
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from .models import User

env = Env()
env.read_env()

key = env('JWT_SECRET_KEY')

class TokenHandler():
  @staticmethod
  def token_decode(auth_header:str=None):
    """
    Split value from Authorization header and decode them
    """
    jwt_token = auth_header.split()[1]
    return jwt.decode(jwt_token, key, algorithms="HS256")

class UserAuthentication(BaseAuthentication):
  """
  Return user ID from request Authorization header
  """
  def authenticate(self, request):
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    if not auth_header:
      return None
    jwt_payload = TokenHandler.token_decode(auth_header)
    return (jwt_payload['id'], None)
