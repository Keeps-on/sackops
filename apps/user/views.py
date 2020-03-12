from django.shortcuts import render,render_to_response

from django.http import JsonResponse, HttpResponse


# Create your views here.


def user_list(request):
    """
    用户管理：查看用户
    :param request:
    :return:
    """
    return render_to_response(template_name='user/user_list.html')
