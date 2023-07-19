from django.db import models

class Person(models.Model):
    date_of_birth = models.DateField()
    age = models.IntegerField(null=True)
