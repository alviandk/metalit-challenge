from django.conf import settings
from django.urls import path, include
from rest_framework import routers
from .views import ChallengeView, GenerateJWTMockup, TaskVerificationView, TaskView, ChallengeTaskView, TestJWTResponse, UnverifiedTaskVerificationView, UserChallengeIndividualView, UserChallengeListView, UserTaskListCompletedView, UserTaskListUncompletedView, UserTaskListView, VerifiedTaskVerificationView

urlpatterns = [
    path('challenge', ChallengeView.as_view()),
    path('task/<int:challenge_id>', TaskView.as_view()),
    path('challenge-task/<int:challenge_id>', ChallengeTaskView.as_view()),

    ### Endpoint related to task verification ###
    path('task-verification', TaskVerificationView.as_view()),
    path('task-verification/verified', VerifiedTaskVerificationView.as_view()),
    path('task-verification/unverified', UnverifiedTaskVerificationView.as_view()),

    ### Endpoint related to user challenge ###
    path('user-challenge/challenge:<int:challenge_id>', UserChallengeIndividualView.as_view()), #Auth, Perm
    path('user-challenge/all', UserChallengeListView.as_view()), #Auth

    ### Endpoint related to user task ###
    path('user-task/challenge:<int:challenge_id>', UserTaskListView.as_view()), #Auth
    path('user-task/challenge:<int:challenge_id>/completed', UserTaskListCompletedView.as_view()), #Auth
    path('user-task/challenge:<int:challenge_id>/uncompleted', UserTaskListUncompletedView.as_view()), #Auth

]

"""
Additional API for dev mode
"""
if settings.DEV_MODE:
    # if dev mode is set to true in env var, add this additional endpoint
    urlpatterns += [
        ### Endpoint to generate JWT token mockup
        path('auth/generate-token/<int:user_id>', GenerateJWTMockup.as_view()),
        path('auth/test-token', TestJWTResponse.as_view()),
    ]
