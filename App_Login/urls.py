from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('', views.sign_up_form, name='sign_up'),
    path('login/', views.login_page, name='login'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('user/<username>/', views.user, name='user'),
    path('follow/<username>/', views.follow, name='follow'),
    path('unfollow/<username>/', views.unfollow, name='unfollow'),
]
