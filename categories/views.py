from django.shortcuts import render, get_object_or_404
from .models import Category

# Create your views here.
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    projects = category.projects.all()

    context = {
        'category': category,
        'projects': projects,
    }
    return render(request, 'categories/category_projects.html', context)