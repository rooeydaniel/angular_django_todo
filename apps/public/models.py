from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=4000)
    create_date = models.DateTimeField(blank=False, null=False)
    completed = models.BooleanField(default=0)

    def __unicode__(self):
        return self.title
