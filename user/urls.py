from django.urls import path

from user import views

urlpatterns = [
    path('my-profile/', views.my_profile, name='my-profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
]
