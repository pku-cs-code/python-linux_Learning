#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render,HttpResponse

# Create your views here.
from webchat import models
from django.contrib.auth.decorators import login_required
import queue,json,time,hashlib,os
from django.core.cache import cache

GLOBAL_MSG_QUEUES = {
    # "id": queue.Queue(),
}


@login_required
def dashboard(request):


    return render(request,'webchat/dashboard.html')

@login_required
def send_msg(request):

    print(request.POST)
    print(request.POST.get('msg'))

    #if request.POST.get()

    msg_data = request.POST.get('data')
    if msg_data:
        msg_data = json.loads(msg_data)
        print(msg_data)
        print(type(msg_data))
        msg_data['timestamp'] = time.time()
        if msg_data['type'] == 'single':
            if not GLOBAL_MSG_QUEUES.get(int(msg_data['to'])):
                GLOBAL_MSG_QUEUES[int(msg_data["to"])] = queue.Queue()#这里要转成int类型，因为前端返回的是字符串格式
            GLOBAL_MSG_QUEUES[int(msg_data["to"])].put(msg_data)
        else:#group
            group_obj = models.WebGroup.objects.get(id=int(msg_data['to']))
            for member in group_obj.members.select_related():
                if not GLOBAL_MSG_QUEUES.get(member.id):#如果字典里不存在这个用户的id则创建一个
                    GLOBAL_MSG_QUEUES[member.id] = queue.Queue()  # 这里要转成int类型，因为前端返回的是字符串格式
                if member.id != request.user.userprofile.id:
                    GLOBAL_MSG_QUEUES[member.id].put(msg_data)



    print(GLOBAL_MSG_QUEUES)
    # #if not GLOBAL_MSG_QUEUES.get():

    return HttpResponse('--msg received---')

def get_new_msgs(request):
    if request.user.userprofile.id not in GLOBAL_MSG_QUEUES:
        print('no queue for user [%s]' %request.user.userprofile.id,request.user)
        GLOBAL_MSG_QUEUES[request.user.userprofile.id] = queue.Queue()
    msg_count = GLOBAL_MSG_QUEUES[request.user.userprofile.id].qsize()
    q_obj = GLOBAL_MSG_QUEUES[request.user.userprofile.id]
    msg_list = []
    #print(type(request.user.userprofile.id))

    if msg_count > 0:
        for msg in range(msg_count):
            msg_list.append(q_obj.get())

        print("new msgs:",msg_list)

    else:#没消息挂起
        print("no new msg for",request.user,request.user.userprofile.name)
        # print(GLOBAL_MSG_QUEUES)

        # wait_new_msg = q_obj.get(timeout=60)
        # if wait_new_msg:#如果返回不为空，代表wait_new_msg是新消息。超时返回为空。不阻塞有两种情况，超时和
        #     msg_list.append(wait_new_msg)

        try:
            msg_list.append(q_obj.get(timeout=60))
        except queue.Empty:
            print("\033[41;1mTIMEOUT  no msg for [%s][%s]\033[0m" %(request.user,request.user.userprofile.id))
    print("msg_list",msg_list)
    return HttpResponse(json.dumps(msg_list))

# def file_upload(request):
#     print(request.POST,request.FILES)
#     file_obj = request.FILES.get('file')
#     new_file_name = "uploads/%s" %file_obj.name
#
#     with open(new_file_name,'wb') as new_file_obj:
#         for chunk in file_obj.chunks():
#             new_file_obj.write(chunk)
#
#
#
#     return  HttpResponse('sucess')

def delete_cache_key(request):
    cache_key = request.GET.get('cache_key')
    cache.delete(cache_key)
    return  HttpResponse("cache key [%s] got deleted") %cache_key


def file_upload(request):
    # if request.method == 'POST':
        print(request.POST,request.FILES)
        file_obj = request.FILES.get('file')
        user_home_dir = "uploads/%s" %request.user.userprofile.id
        if not os.path.isdir(user_home_dir):
            os.mkdir(user_home_dir)

        new_file_name = "%s/%s" %(user_home_dir,file_obj.name)
        recv_size = 0
        with open(new_file_name,'wb') as new_file_obj:
            for chunk in file_obj.chunks():
                new_file_obj.write(chunk)
                recv_size += len(chunk)
                cache.set(file_obj.name,recv_size)
        return HttpResponse("---file upload success--")

def file_upload_progress(request):
    filename = request.GET.get('filename')
    print("filename of file_upload_progress:",filename)
    progress = cache.get(filename)
    print("type of progress:-->",type(progress))
    print("print progress of cache.get(filename):-->",filename,progress)

    return HttpResponse(json.dumps({"recv_size":progress}))