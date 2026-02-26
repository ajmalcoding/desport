from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import DesignerProfile

# Create your views here.
def designer_profile(request, username):
    user = get_object_or_404(User, username=username)
    designer = get_object_or_404(DesignerProfile, user=user)
    projects = designer.projects.all()
    services = designer.services.all()
    projects_count = designer.projects.count()
    
    context = {
        'designer': designer,
        'projects': projects,
        'services': services,
        'projects_count': projects_count,
    }
    return render(request, "designer_profile.html", context)