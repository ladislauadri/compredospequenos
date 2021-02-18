
import os
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

from taggit_selectize.managers import TaggableManager


from .formatChecker import FileValidator


validate_file = FileValidator(max_size=1024 * 1024 * 100, 
                             content_types=(
                                'video/x-msvideo',
                                'image/bmp','image/gif',
                                'image/jpeg', 
                                'video/quicktime', 
                                'application/pdf',  
                                'video/mp4', 
                                'video/mpeg', 
                                'audio/mpeg', 
                                'image/png',))


class Post(models.Model):
    description = models.CharField(max_length=1000, blank=True)
    content = models.FileField(upload_to='uploads/', blank=True, null=True, validators=[validate_file])
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    publishedAt = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    type = models.CharField(max_length=1000, default='post')


    def __str__(self):
        return str(self.id) + ' ' + self.description


    def get_absolute_url(self):
        return reverse('post:post', kwargs={'pk': self.pk})
