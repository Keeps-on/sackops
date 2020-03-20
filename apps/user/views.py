from django.shortcuts import render, render_to_response

from django.http import JsonResponse, HttpResponse

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
    data = UserProfile.objects.values()[page_start:page_end]
    count = data.count()
    result['data'] = list(data)
    result['count'] = count
    return JsonResponse(result)


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
