from django.db import models

class Movie_Details(models.Model):
    title=models.CharField(max_length=50)
    release_date=models.CharField(max_length=50)
    video_link=models.CharField(max_length=1000)
    banner=models.CharField(max_length=1000,default='#')

    def __str__(self):
        return self.title

