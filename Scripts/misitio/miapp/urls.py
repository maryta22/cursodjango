from django.urls import path, re_path
from .views import home, post_list
from . import views

urlpatterns = [
    path('home/', post_list),
    re_path(r"home/% url 'newpost' %", views.newpost, name="newpost")
]
