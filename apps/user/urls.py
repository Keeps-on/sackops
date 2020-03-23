from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('list/', views.user_list, name='user_list'),  # 用户列表
    path('data/', views.user_data, name='user_data'),  # 用户数据表格渲染
    path('create/', views.user_create, name='user_create'),  # 创建用户
    path('update/', views.user_update, name='user_update'),  # 创建用户

    # 角色相关
    path('role/', views.role_list, name='role_list'),
    path('role/create/', views.role_create, name='role_create'),
    path('role/data/', views.role_data, name='role_data'),
    # 用户绑定角色
    path('role/add', views.user_add_role, name='user_add_role'),
    path('role/remove', views.user_remove_role, name='user_remove_role')
]
