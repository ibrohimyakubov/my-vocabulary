from django.urls import path

from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-department/', views.add_deparment, name='add-department'),
    path('add-unit/', views.add_unit, name='add-unit'),
    path('department/<uuid:uuid>/', views.department_detail, name='department'),
    path('unit/<uuid:uuid>/', views.unit_vocabulary, name='unit-vocabulary'),
]
