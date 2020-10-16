import datetime

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/images/')
    date = models.DateField(default=datetime.datetime.now())
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
