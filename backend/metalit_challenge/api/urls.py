from django.urls import path, include
from rest_framework import routers
from .views import ChallengeView, TaskView, ChallengeTaskView, TaskVerificationViewSet

router = routers.DefaultRouter()
router.register(r'task-verification', TaskVerificationViewSet, basename='task-verification')

urlpatterns = [
    path('', include(router.urls)),
    path('challenge', ChallengeView.as_view()),
    path('task/<int:challenge_id>', TaskView.as_view()),
    path('challenge-task/<int:challenge_id>', ChallengeTaskView.as_view()),
]
