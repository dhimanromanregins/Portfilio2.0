from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('project_details/', views.project_detail, name='project_details')
]