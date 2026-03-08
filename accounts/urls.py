from django.urls import path
from . import views

urlpatterns = [
    path('designers_listing/', views.designers_list, name='designers_list'),
    path('<str:username>/', views.designer_profile, name='designer_profile'),
]
