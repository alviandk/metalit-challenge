from django.urls import path, include
from rest_framework import routers
from .views import ChallengeView, GenerateJWTMockup, TaskVerificationView, TaskView, ChallengeTaskView, UnverifiedTaskVerificationView, UserChallengeIndividualView, UserChallengeListView, UserTaskListCompletedView, UserTaskListUncompletedView, UserTaskListView, VerifiedTaskVerificationView

urlpatterns = [
    path('challenge', ChallengeView.as_view()),
    path('task/<int:challenge_id>', TaskView.as_view()),
    path('challenge-task/<int:challenge_id>', ChallengeTaskView.as_view()),

    ### Endpoint related to task verification ###
    path('task-verification', TaskVerificationView.as_view()),
    path('task-verification/verified', VerifiedTaskVerificationView.as_view()),
    path('task-verification/unverified', UnverifiedTaskVerificationView.as_view()),

    ### Endpoint related to user challenge ###
    path('user-challenge/<int:user_id>', UserChallengeIndividualView.as_view()),
    path('user-challenge/all/<int:user_id>', UserChallengeListView.as_view()),

    ### Endpoint related to user task ###
    path('user-task/<int:user_id>/challenge:<int:challenge_id>', UserTaskListView.as_view()),
    path('user-task/<int:user_id>/challenge:<int:challenge_id>/completed', UserTaskListCompletedView.as_view()),
    path('user-task/<int:user_id>/challenge:<int:challenge_id>/uncompleted', UserTaskListUncompletedView.as_view()),

    ### Endpoint to generate JWT token mockup
    path('auth/generate-token', GenerateJWTMockup.as_view()),
]
