from django.urls import path, include
from rest_framework import routers
from .views import ChallengeView, TaskVerificationView, TaskView, ChallengeTaskView, UnverifiedTaskVerificationView, VerifiedTaskVerificationView

urlpatterns = [
    path('challenge', ChallengeView.as_view(), name="challenge"),
    path('task/<int:challenge_id>', TaskView.as_view(), name="task"),
    path('challenge-task/<int:challenge_id>', ChallengeTaskView.as_view()),

    ### Endpoint related to task verification ###
    path('task-verification', TaskVerificationView.as_view()),
    path('task-verification/verified', VerifiedTaskVerificationView.as_view()),
    path('task-verification/unverified', UnverifiedTaskVerificationView.as_view()),
]
