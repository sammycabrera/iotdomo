from django.urls import path
from . import views


urlpatterns = [
    path("location/",views.Locations_method.as_view(),name="location"),
    path("location/<int:codigo>/",views.Locations_method.as_view(),name="location_put"),
    path("location/all/",views.Locations_Id_method.as_view(),name="location_id"),
    path("device/",views.Devices_method.as_view(),name="device"),
    path("device/<int:codigo>/",views.Devices_method.as_view(),name="device_put"),
    path("device/all/",views.Devices_Id_method.as_view(),name="device_id"),
    path("dot/",views.Dots_method.as_view(),name="dot"),
    path("dot/<int:codigo>/",views.Dots_method.as_view(),name="dot_put"),
    path("dot/all/",views.Dots_Id_method.as_view(),name="dot_id"),
]