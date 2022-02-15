from django.urls import path
from . import views
urlpatterns = [
    path('', views.leave_list_view, name='home'),
    path('new/leave/request', views.new_leave_request, name='new_leave'),
    path('<id>/update', views.update_leave_request, name='update_leave' ),
]
