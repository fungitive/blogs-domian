from django.urls import path
from .views import index, blog_list, blog_detail

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('list/', blog_list, name='list'),
    path('detail/<str:blog_id>/', blog_detail, name='detail'),
]
