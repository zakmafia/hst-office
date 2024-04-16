from django.urls import path
from . import views

urlpatterns = [
    path('', views.help_desk, name='help_desk'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('knowledge-base/', views.knowledge_base, name='knowledge_base')
]
