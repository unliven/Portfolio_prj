from django.db import models
from django.forms import CheckboxInput


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portf/images/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="portf/certificates/")
    landscape = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Recommendation(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="portf/recommendations/")

    def __str__(self):
        return self.title
