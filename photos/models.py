from django.db import models
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager

class Photo(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField(default=timezone.now)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title


