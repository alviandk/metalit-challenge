from django.db.models.constraints import UniqueConstraint
from django.utils.translation import gettext_lazy as _
from django.db import models

class Challenge(models.Model):
    """
    Model for challenge table in database
    """
    class Status(models.TextChoices):
      PUBLISHED = 'published', _('published')
      UNPUBLISHED = 'unpublished', _('unpublished')

    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=11, choices=Status.choices, default=Status.UNPUBLISHED, null=False)
    budget = models.PositiveIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
      return f"{self.name}"

class Task(models.Model):
  """
  Model for task table in database
  """
  challenge = models.ForeignKey(
    'Challenge', 
    on_delete = models.CASCADE,
  )
  name = models.CharField(max_length=255, null=False)
  description = models.TextField(blank=True, null= True)
  reward_amount = models.PositiveIntegerField(null=False)
  created_at = models.DateTimeField(auto_now_add=True, null=False)

  def __str__(self):
    return f"{self.name}"

class User(models.Model):
  """
  Model for user mockup
  """
  name = models.CharField(max_length=255, null=False)

class TaskVerification(models.Model):
  """
  Model for task_verification table in database
  """
  class Status(models.TextChoices):
      TRUE = 'true', _('true')
      FALSE = 'false', _('false')
  challenge = models.ForeignKey(
    'Challenge', 
    on_delete = models.CASCADE,
  )
  task = models.ForeignKey(
    'Task',
    on_delete = models.CASCADE
  )
  submission = models.TextField(blank=True, null= True)
  is_verified = models.CharField(max_length=5, choices=Status.choices, default=Status.FALSE, null=False)
  verified_at = models.DateTimeField(default=None, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True, null=False)

  def __str__(self):
    return f"{self.created_at}"

class UserChallenge(models.Model):
  """
  Model for user_challenge table in database
  """
  #TODO: django only support 1 primary key (?)
  class Meta:
    constraints = [
      UniqueConstraint('challenge', 'user', name='unique_challenge_user')
    ]

  class Status(models.TextChoices):
    COMPLETED = 'completed', _('completed')
    UNCOMPLETED = 'uncompleted', _('uncompleted')
  challenge = models.ForeignKey(
    'Challenge',
    on_delete = models.CASCADE
  )
  user = models.ForeignKey(
    'User',
    on_delete = models.CASCADE
  )
  status = models.CharField(max_length=11, choices=Status.choices, default=Status.UNCOMPLETED, null=False)
  completed_at = models.DateTimeField(default=None, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True, null=False)

class UserTask(models.Model):
  """
  Model for user_task table in database
  """
  #TODO: django only support 1 primary key (?)
  class Meta:
    constraints = [
      UniqueConstraint('task', 'user', name='unique_task_user')
    ]

  class Status(models.TextChoices):
    COMPLETED = 'completed', _('completed')
    UNCOMPLETED = 'uncompleted', _('uncompleted')
  task = models.ForeignKey(
    'Task',
    on_delete = models.CASCADE
  )
  user = models.ForeignKey(
    'User',
    on_delete = models.CASCADE
  )
  status = models.CharField(max_length=11, choices=Status.choices, default=Status.UNCOMPLETED, null=False)
  completed_at = models.DateTimeField(default=None, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True, null=False)