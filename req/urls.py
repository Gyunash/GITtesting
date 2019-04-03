from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
]