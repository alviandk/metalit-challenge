from django.urls import path
from .views import ChallengeView, TaskView

urlpatterns = [
    path('challenge', ChallengeView.as_view()),
    path('task', TaskView.as_view()),
]
