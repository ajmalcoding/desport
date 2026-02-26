from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def project_detail_view(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)

    context = {
        'project': project,
        'images': project.images.all(),
    }

    return render(request, 'portfolios/project_detail_view.html', context)