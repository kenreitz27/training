from django.urls import path
from . import views

urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("post-<int:event_pk>/", views.post_info, name="post_info"),
    path("view/", views.view_info, name="view_info"),
    path("monitor-<int:event_pk>/", views.event_monitor, name="event_monitor")
]