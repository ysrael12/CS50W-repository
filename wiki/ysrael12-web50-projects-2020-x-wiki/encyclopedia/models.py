from django.db import models

# Create your models here.
class postwiki (models.Model):
    #title = models.CharField (max_length= 100)
    postwiki = models.CharField(max_length=100000)


def __str__(self):
    return self.title
