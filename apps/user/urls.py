from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('list/', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),

]
