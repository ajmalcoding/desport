from django.urls import path
from . import views

urlpatterns = [
    # path('<slug:project_slug>/', views.project_detail_view, name='project_detail_view'),
    path('<str:username>/', views.designer_profile, name='designer_profile'),
]
