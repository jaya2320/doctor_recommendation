from django.urls import path,include
from . import views
urlpatterns = [
    path('doctors/',views.doctors.as_view())
]