from django.shortcuts import render, render_to_response

from django.http import JsonResponse, HttpResponse
from common import keys
from django.core.cache import cache

from user.models import UserProfile, Role
from common.utils import send_mail_async, send_mail_attach_async, send_mail_html_async


# 测试邮件发送
# send_mail_async()
# send_mail_attach_async()
# send_mail_html_async()

# Create your views here.
###################################
#          用户相关                #
###################################

def user_list(request):
    """
    用户管理：查看用户
    :param request:
    :return:
    """
    return render_to_response(template_name='user/user_list.html')


def user_data(request):
    """
    表格渲染
    :param request:
    :return:
    """
    page = int(request.GET.get('page', default=1))
    limit = int(request.GET.get('limit', default=10))
    # 分页
    page_start = (page - 1) * limit
    page_end = page_start + limit
    # 返回结果
    result = {
        "code": 0,
        "msg": "",
    }
    # 增加缓存层
    key = keys.USER_KEY % 'profile_data'
    profile_data = cache.get(key)
    print(profile_data)
    if profile_data is None:
        print("数据库获取")
        profile_data = UserProfile.objects.values()
        cache.set(key, profile_data)  # 将数据添加到缓存

    data = profile_data[page_start:page_end]
    print(data)
    count = profile_data.count()
    result['data'] = list(data)
    result['count'] = count
    return JsonResponse(result)

# TODO 对于新增用户需要更新缓存
# https://www.jianshu.com/p/e3c640e2482c
# https://www.cnblogs.com/robinunix/articles/10614369.html
def user_create(request):
    """
    添加用户
    :param request:
    :return:
    """
    result = {"code": 0, "msg": ""}
    # 获取用户信息
    username = request.GET.get('username')
    password = request.GET.get('password')
    # 存入数据
    UserProfile.objects.create(username=username, password=password)
    return JsonResponse(result)


def user_update(request):
    """
    修改用户
    :param request:
    :return:
    """
    result = {"code": 0, "msg": ""}
    # 修改用户信息
    user_id = request.GET.get('user_id')
    username = request.GET.get('username')
    password = request.GET.get('password')
    print(user_id, username, password)
    # 修改用户
    UserProfile.objects.filter(id=user_id).update(username=username, password=password)
    return JsonResponse(result)


def user_add_role(request):
    """
    用户添加角色
    :param request:
    :return:
    """
    


def user_move_role(request):
    """
    用户移除角色
    :param request:
    :return:
    """



###################################
#          角色相关                #
###################################

def role_list(request):
    """
    角色列表
    :param request:
    :return:
    """
    return render_to_response(template_name='user/role_list.html')


def role_data(request):
    page = int(request.GET.get('page', default=1))
    limit = int(request.GET.get('limit', default=10))
    # 分页
    page_start = (page - 1) * limit
    page_end = page_start + limit
    # 返回结果
    result = {
        "code": 0,
        "msg": "",
    }
    data = Role.objects.values()[page_start:page_end]
    count = data.count()
    result['data'] = list(data)
    result['count'] = count
    return JsonResponse(result)


def role_create(request):
    result = {"code": 0, "msg": ""}
    # 角色名称
    name = request.GET.get('role_name')
    # 创建角色
    Role.objects.create(name=name)
    return JsonResponse(result)
