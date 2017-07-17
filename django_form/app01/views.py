from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    print(request.POST)
    print(request.GET)
    print(request.FILES)
    return HttpResponse('ok')

