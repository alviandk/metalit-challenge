from django.contrib import admin
from .models import Challenge, Task, TaskVerification, User

# Register your models here.

admin.site.register(Challenge)
admin.site.register(Task)
admin.site.register(TaskVerification)
admin.site.register(User)