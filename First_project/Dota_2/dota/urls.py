from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('about/', about, name='about'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<int:post_id>/', show_post, name='post'),

]
