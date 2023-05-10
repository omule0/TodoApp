from django.urls import path, re_path
from . import views

urlpatterns = [
        path('', views.landing_page, name='landing_page'),
        path('delete_task/<int:name_id>/', views.deleteTask, name='deleteTask'),
        path('add_task/', views.add_task, name='add_task'),
        path('home/', views.home, name='home'),
        path('update_task/<int:name_id>/', views.updateTask, name='updateTask'),
        path('crossoff/<int:name_id>', views.cross_off, name='cross_off'),
        path('uncross/<int:name_id>', views.uncross, name='uncross'),
        re_path(r'^home/sticky_notes/$', views.sticky_notes, name='sticky_notes'),

]
