from django.urls import path

from . import views

urlpatterns = [
    path('device/new/', views.new_device, name='new_device'),
    path('device/<int:pk>/', views.detail_device, name='detail_device'),
    path('device/<int:code>/edit/', views.edit_device, name='edit_device'),
    # path('device/<int:code>/delete/', views.delete_device, name='delete_device'),
]
