from django.shortcuts import render, get_object_or_404
from .models import Category
from django.core.paginator import Paginator

# Create your views here.
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    projects = category.projects.all()
    paginator = Paginator(projects, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'projects': page_obj,
    }
    return render(request, 'categories/category_projects.html', context)