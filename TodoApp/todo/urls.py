from django.urls import path, re_path
from . import views

urlpatterns = [
        path('', views.landing_page, name='landing_page'),
        re_path(r'^home/$', views.home, name='home'),
        re_path(r'^add_task/$', views.add_task, name='add_task'),
        re_path(r'^home/sticky_notes/$', views.sticky_notes, name='sticky_notes'),
]