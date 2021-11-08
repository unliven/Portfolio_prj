from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.title