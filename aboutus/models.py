from django.db import models

# Create your models here.
class About(models.Model):

    def __str__(self):
        return self.title