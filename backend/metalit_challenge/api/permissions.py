from .serializers import UserSerializer
from rest_framework import permissions

class IsOwnerObjectPermission(permissions.BasePermission):
  """
  Permission to allow read, write, or edit if the object belongs to the owner of the request
  """

  def has_permission(self, request, view):
    """
    Override has_permission method
    """

    # if the user is authenticated
    return request.user
  
  def has_object_permission(self, request, view, obj):
    """
    Override has_object_permission method
    """

    user_obj = request.user[0]
    serializer = UserSerializer(user_obj, many=False)

    user_id = request.user[0].id

    # check if user is accessing legal object 
    if (user_id == obj.user_id):
      return True
    return False

