"""lockerweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from django.urls import path
from lockerweb import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.user_list, name='user_list'),
    path('capture_users/', views.capture_user, name='capture_user'),
    path('create_users/', views.create_user, name='create_user'),
    path('login/', views.login, name='login'),
    path('authenticate_staff/', views.authenticate_staff, name='authenticate_staff'),
    path('front_desk/', views.front_desk, name='front_desk'),
    path('assign/<locker_id>/<user_name>', views.assign_locker, name='assign_locker'),
    path('user_profile/<str:email>/', views.user_profile, name='user_profile'),
    path('locker/<locker_id>/popup/', views.locker_menu, name='locker_menu'),
    path('locker/<locker_id>/popup_user/', views.locker_menu_user, name='locker_menu_user'),
    path('success/', views.success, name='success'),
    #path('front_desk/', views.create_user, name='create_user'),
    path('locker/<locker_id>/popup_staff/', views.search_user, name='search_user'),
    path('locker/<locker_id>/popup_rent/<user_id>', views.locker_menu_staff_rent_confirm, name='locker_menu_staff_rent_confirm'),
    path('locker/<locker_id>/popup_staff_release/', views.locker_menu_staff_release, name='locker_menu_staff_release'),
    path('locker/<locker_id>/popup_staff_release_confirm/', views.locker_menu_staff_release_confirm, name='locker_menu_staff_release_confirm'),
]
