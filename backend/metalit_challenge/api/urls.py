from django.urls import path
from .views import ChallengeView, TaskView

urlpatterns = [
    path('challenge', ChallengeView.as_view()),
    path('task/<int:challenge_id>', TaskView.as_view()),
]
