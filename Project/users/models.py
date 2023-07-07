from django.db import models
from django.contrib.auth.models import User

class Position(models.Model):
    position = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.position
    
    class Meta:
        ordering = ['id']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']