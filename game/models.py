from django.db import models

class Game_Details(models.Model):
    title=models.CharField(max_length=50)
    release_date=models.CharField(max_length=50)
    video_link=models.CharField(max_length=1000)
    banner=models.CharField(max_length=1000,default='#')

    def __str__(self):
        return self.title
class Game_carousel(models.Model):
    caption=models.CharField(max_length=50)
    image_link=models.CharField(max_length=200)

    def __str__(self):
        return self.caption