from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import DesignerProfile, Skill
from categories.models import Category
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def designer_profile(request, username):
    user = get_object_or_404(User, username=username)
    designer = get_object_or_404(DesignerProfile, user=user)
    projects = designer.projects.all()
    services = designer.services.all()
    projects_count = designer.projects.count()

    paginator = Paginator(projects, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'designer': designer,
        'projects': page_obj,
        'services': services,
        'projects_count': projects_count,
    }
    return render(request, "designer_profile.html", context)

def designers_list(request):
    search = request.GET.get("q")
    category = request.GET.get("category")
    selected_skill = request.GET.getlist("skill")
    location = request.GET.get("location")

    designers = DesignerProfile.objects.all()

    if search:
        designers = designers.filter(Q(user__username__icontains=search) | Q(name__icontains=search) | Q(location__icontains=search) | Q(categories__name__icontains=search) | Q(title__icontains=search)).distinct()

    if category:
        designers = designers.filter(categories__slug=category)

    if selected_skill:
        designers = designers.filter(skills__slug__in=selected_skill).distinct()

    if location:
        designers = designers.filter(location__icontains=location)

    paginator = Paginator(designers, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    query_params = request.GET.copy()
    query_params.pop('page', None)
    query_string = query_params.urlencode()

    categories = Category.objects.all()
    skills = Skill.objects.all()
    locations = DesignerProfile.objects.exclude(location="").values_list("location", flat=True).distinct()

    context = {
        'designers': page_obj,
        'query_string': query_string,
        'skills': skills,
        'selected_skill':selected_skill,
        'categories': categories,
        'locations': locations,
    }
    return render(request, "designers_listing.html", context)