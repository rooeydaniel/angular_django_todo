from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=4000)
    create_date = models.DateTimeField()

    def __unicode__(self):
        return self.title