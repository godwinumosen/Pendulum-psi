from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Module(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='module_owner')
    hours = models.PositiveIntegerField()
    
    def __str__(self) :
        return self.title