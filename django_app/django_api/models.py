from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):

    class TaskStatus(models.TextChoices):
        INITIATED = "INITIATED", _('Initiated')
        PENDING = "PENDING", _('Pending')
        COMPLETED = "COMPLETED", _('Completed')

    title = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    due_date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
    )

    def __str__(self):
        return f"Task: {self.title}\n Due date: {self.due_date}\n Status: {self.status}"
