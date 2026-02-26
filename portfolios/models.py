from django.db import models
from accounts.models import DesignerProfile
from categories.models import Category
from django.utils.text import slugify

# Create your models here.
class Project(models.Model):
    profile = models.ForeignKey(DesignerProfile, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    highlights = models.TextField(blank=True)
    tools_used = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, related_name='projects')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "projects"
        ordering = ['-created_at']


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/images/')
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"
    
    class Meta:
        db_table = "project_images"
        ordering = ['order']