from django.contrib import admin
from .models import DesignerProfile, Skill, Service

# Register your models here.
admin.site.register(DesignerProfile)
admin.site.register(Skill)
admin.site.register(Service)