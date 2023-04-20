from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="Users-register"),
    path("profile/", views.profile, name="Users-profile"),
]