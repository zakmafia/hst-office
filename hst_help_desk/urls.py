from django.urls import path
from . import views

urlpatterns = [
    path('', views.help_desk, name='help_desk'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('user-requests/', views.user_requests, name='user_requests'),
    path('knowledge-base/', views.knowledge_base, name='knowledge_base')
]
