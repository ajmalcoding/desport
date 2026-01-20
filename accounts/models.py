from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = (
        ('designer', 'Designer'),
        ('client', 'Client'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    categories = models.ManyToManyField('categories.category', related_name='Profile', blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "profile"