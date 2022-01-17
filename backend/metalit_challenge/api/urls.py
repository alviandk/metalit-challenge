from django.conf import settings
from django.urls import include, path
from rest_framework import routers

from .views import (ChallengeTaskView, ChallengeView, CreateUserTaskView, GenerateJWTMockup, CreateUserChallengeView,
                    TaskVerificationView, TaskView, TestJWTResponse,
                    UnverifiedTaskVerificationView,
                    UserChallengeIndividualView, UserChallengeListView, UserChallengeTaskView,
                    UserTaskListCompletedView, UserTaskListUncompletedView,
                    UserTaskListView, VerifiedTaskVerificationView)

urlpatterns = [
    path('challenge', ChallengeView.as_view(), name="challenge"),
    path('task/<int:challenge_id>', TaskView.as_view(), name="task"),
    path('challenge-task/<int:challenge_id>', ChallengeTaskView.as_view()),

    ### Endpoint related to task verification ###
    path('task-verification', TaskVerificationView.as_view(), name="task_verification"),
    path('task-verification/verified', VerifiedTaskVerificationView.as_view()),
    path('task-verification/unverified', UnverifiedTaskVerificationView.as_view()),

    ### Endpoint related to user challenge ###
    path('user-challenge/challenge:<int:challenge_id>', UserChallengeIndividualView.as_view(), name="user-challenge-individual"), #Auth, Perm
    path('user-challenge/all', UserChallengeListView.as_view(), name="user-challenge-all"), #Auth
    path('user-challenge/create', CreateUserChallengeView.as_view(), name="user-challenge-creation"),

    ### Endpoint related to user task ###
    path('user-task/challenge:<int:challenge_id>', UserTaskListView.as_view(), name="user-task-all"), #Auth
    path('user-task/challenge:<int:challenge_id>/completed', UserTaskListCompletedView.as_view(), name="user-task-completed"), #Auth
    path('user-task/challenge:<int:challenge_id>/uncompleted', UserTaskListUncompletedView.as_view(), name="user-task-uncompleted"), #Auth
    path('user-task/create', CreateUserTaskView.as_view()),

    ### Endpoint related to user challenge and task ###
    path('user-challenge-task/challenge/<int:challenge_id>/<int:user_id>', UserChallengeTaskView.as_view()),
]

"""
Additional API for dev mode
"""
if settings.DEV_MODE:
    # if dev mode is set to true in env var, add this additional endpoint
    urlpatterns += [
        ### Endpoint to generate JWT token mockup
        path('auth/generate-token/<int:user_id>', GenerateJWTMockup.as_view(), name="generate-token"),
        path('auth/test-token', TestJWTResponse.as_view()),
    ]
