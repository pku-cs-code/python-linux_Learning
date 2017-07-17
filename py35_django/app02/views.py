from django.shortcuts import render,HttpResponse

# Create your views here.


def home(request):
    #django的返回请求需要封装在HttpResponse中
    return HttpResponse('app02')