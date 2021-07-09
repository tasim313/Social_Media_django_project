from django.urls import path
from . import views
app_name = 'App_Posts'

urlpatterns = [
      path('home/', views.home, name='home')
]