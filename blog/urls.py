from django.urls import path

from .views import blog, blog_list

urlpatterns = [
    path("", blog),
    path("/list", blog_list),
]