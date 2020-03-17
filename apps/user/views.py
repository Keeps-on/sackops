from django.shortcuts import render, render_to_response

from django.http import JsonResponse, HttpResponse


from user.models import UserProfile


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
    UserProfile.objects.create(username=username,password=password)
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
