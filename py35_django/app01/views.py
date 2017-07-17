from django.shortcuts import render

from django.shortcuts import HttpResponse
from app01 import models

# Create your views here.

def db_handle(request):
    #request封装了用户的所有请求
    # request.POST#用户以POST方式发送过来的数据
    # request.GET#用户以GET方式发送过来的数据
    #默认是以get方式

    #增
    #models.UserInfo.objects.create(username='eric',password='123',age=18)
    # dic = {"username":"alex","password":"123","age":17}
    # models.UserInfo.objects.create(**dic)

    #删
    # models.UserInfo.objects.filter(username='alex').delete()

    #改
    #models.UserInfo.objects.all().update(age=20)

    #查
    #models.UserInfo.objects.filter(age=20).first()

    if request.method == 'POST':
        print(request.POST)

        #取数据
        # request.POST.get
        # request.POST['username']
        #request.POST['age'] = int(request.POST['age'])
        models.UserInfo.objects.create(username=request.POST['username'],
                                       password=request.POST['password'],
                                       age=request.POST['age'])


    user_list_obj = models.UserInfo.objects.all()
    #queryset,list类型
    # for line in user_list_obj:
    #     print(line.username,line.password)

    #return HttpResponse('db_ok')
    return render(request,'t1.html',{'li':user_list_obj})#打开t1.html文件，将里面的内容用user_list_obj替换


def home(request):
    #django的返回请求需要封装在HttpResponse中
    return HttpResponse('app01')

def news(request, nid1, nid2):#url传来的字符串
    nid = nid1 + nid2
    return HttpResponse(nid)

def page(request, n2, n1):#url传来的字符串
    nid = n1 + n2
    return HttpResponse(nid)


