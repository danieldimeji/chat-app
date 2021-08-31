from django.urls import path
from . import views


urlpatterns = [

    path('', views.home_view, name='home'),
    path('settings/', views.settings_view, name='settings'),
    path('groups/', views.groups_view, name='groups'),
    path('status/', views.status_view, name='status'),
    path('calls/', views.calls_view, name='calls'),
    path('archived/', views.archived_view, name='archived'),

]
