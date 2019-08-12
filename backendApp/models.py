from django.db import models
from djongo.models.fields import ObjectIdField


# Create your models here.
class Specs(models.Model):
    _id = ObjectIdField()
    name = models.TextField()
    description = models.TextField()
    pingUrl = models.TextField()
    interval = models.IntegerField()
    waitTime = models.IntegerField()
    status = models.BooleanField(default=False)
