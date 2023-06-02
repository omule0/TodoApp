from django.urls import path
from . import views

urlpatterns = [
        path('', views.landing_page, name='landing_page'),
        path('delete_task/<int:name_id>/', views.deleteTask, name='deleteTask'),
        path('add_task/', views.add_task, name='add_task'),
        path('home/', views.home, name='home'),
        path('updateTask/<int:name_id>/', views.updateTask, name='updateTask'),
        path('crossoff/<int:name_id>', views.cross_off, name='cross_off'),
        path('uncross/<int:name_id>', views.uncross, name='uncross'),
        path('delete_old_tasks/', views.delete_old_tasks, name='delete_old_tasks'),
        #path('mark_skipped_tasks/', views.mark_skipped_tasks, name='mark_skipped_tasks'),
        path('home/upcoming/', views.tasks_today, name='tasks_today'),
        path('home/weekly/', views.weekly, name='weekly'),
        path('week_crossoff/<int:item_id>', views.week_cross_off, name='week_cross_off'),
        path('weekuncross/<int:item_id>', views.weekuncross, name='weekuncross'),
        path('deleteList/<int:item_id>/',views.deleteList, name='deleteList'),
        path('delete_old_weekly_tasks/', views.delete_old_weekly_tasks, name='delete_old_weekly_tasks'),
        path('home/sticky_notes/', views.sticky_notes, name='sticky_notes'),
        path('home/profile_pic/', views.profile_pic, name='profile_pic'),
        path('home/calendar/', views.calendars, name='calenders'),
]
