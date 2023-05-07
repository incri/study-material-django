from django.db import models
from django.conf import settings


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
