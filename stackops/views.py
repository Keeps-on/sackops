


from django.shortcuts import render, render_to_response, redirect, resolve_url, reverse
from django.http import JsonResponse, HttpResponse


# Create your views here.


def index(request):
    """
    首页
    :param request:
    :return:
    """
    return render_to_response(template_name='index.html')