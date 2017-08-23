#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render,HttpResponse

# Create your views here.
from webchat import models
from django.contrib.auth.decorators import login_required
import queue,json,time

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
    return HttpResponse(json.dumps(msg_list))


