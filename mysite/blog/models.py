# blog/models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to = 'intruder_image/%Y/%m/%d/',null=True, blank=True)
    
    def publish(self):
        self.published_date = time.now()
        self.save()
    
    def __str__(self):
        return self.title
