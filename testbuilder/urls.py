from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'testbuilder'
urlpatterns = [
    # ex: /itembank/
    path('', views.index, name='tests'),
    path('testbuilder/', views.index, name='tests'),
    path('ajax/selected_test/', views.selected_test, name='selected_test'),
]
