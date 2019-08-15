from django.urls import path
from . import views

urlpatterns = [
  path("", views.core_index, name="core_index"),
  path("signup/", views.core_signup, name="core_signup"),
  path("login/", views.core_login, name="core_login"),
]