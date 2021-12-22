from django.urls import path
from .views import ChallengeView, TaskView, ChallengeTaskView

urlpatterns = [
    path('challenge', ChallengeView.as_view()),
    path('task/<int:challenge_id>', TaskView.as_view()),
    path('challengetask/<int:challenge_id>', ChallengeTaskView.as_view()),
]
