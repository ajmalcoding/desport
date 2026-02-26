from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DesignerProfile(models.Model):
    AVAILABILITY_CHOICES = [
        ('Available Now', 'Available Now'),
        ('Unavailable Now', 'Unavailable Now'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='designer_profile')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    categories = models.ManyToManyField('categories.category', related_name='designer_profiles', blank=True)
    availability_status = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available')
    social_links = models.JSONField(default=dict, blank=True)
    skills = models.ManyToManyField('Skill', blank=True)
    tools = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = "designer_profile"

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    designer = models.ForeignKey(DesignerProfile, on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    delivery_time = models.PositiveIntegerField(help_text="Delivery time in weeks")
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.title} - {self.designer.user.username}"