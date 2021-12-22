from django.utils.translation import gettext_lazy as _
from django.db import models

class Challenge(models.Model):
    """
    Model for challenge table in database
    """
    class Status(models.TextChoices):
      PUBLISHED = 'published', _('published')
      UNPUBLISHED = 'unpublished', _('unpublished')

    nama = models.CharField(max_length=255, null=False)
    deskripsi = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=11, choices=Status.choices, default=Status.UNPUBLISHED, null=False)
    budget = models.PositiveIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
      return f"{self.nama}"

class Task(models.Model):
  """
  Model for task table in database
  """
  challenge_id = models.ForeignKey(
    'Challenge', 
    on_delete = models.CASCADE,
  )
  nama = models.CharField(max_length=255, null=False)
  deskripsi = models.TextField(blank=True, null= True)
  reward_amount = models.PositiveIntegerField(null=False)
  created_at = models.DateTimeField(auto_now_add=True, null=False)

  def __str__(self):
    return f"{self.nama}"