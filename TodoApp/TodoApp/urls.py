from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from Users import views as Users_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path("Users/", include('Users.urls')),
    path('', include('todo.urls')),
    path("login/", auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
]
