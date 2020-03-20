from django.shortcuts import render, render_to_response

from django.http import JsonResponse, HttpResponse

from user.models import UserProfile
from common.utils import send_mail_async, send_mail_attach_async, send_mail_html_async


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
    # 测试邮件发送
    # send_mail_async()
    # send_mail_attach_async()
    send_mail_html_async()
    return render_to_response(template_name='user/user_list.html')


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
    return render_to_response(template_name='user/user_list.html')
