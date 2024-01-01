from django.db import models
from django.utils import timezone
class Time(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
def __str__(self):
    return f'{self.content[:50]}'
class Meta:
    ordering = ['-modified_time']    
 



