#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket,time,hashlib
import SocketServer
import os
import json
#from conf import settings


class MyTCPHandler(SocketServer.BaseRequestHandler):\
    ##print('\033[32;1mStarting CrazyFTP server on %s:%s...\n\033[0m' #%(main.help_msg))
    response_code_list = {
        "200":"Pass authentication!",
        "201":"Wrong username or password",
        "202":"Invalid username or password",
        "300":"Ready to send file to client",
        "301":"Client ready to receive file data",
        "302":"File doesn't exist",
    }

    def handle(self):
        while True:
            data = self.request.recv(1024)
            print("-->data:",data)
            if not data:
                print("\033[31;1mHas lost client\033[0m",self.client)
                break#如果收不到客户端数据了，代表客户端断开
            self.instruction_allowcation(data)#客户端发过来的数据统一交给指令分发器处理

    def instruction_allowcation(self,instructions):

        instructions = instructions.split("|")
        function_str = instructions[0]
        if hasattr(self,function_str):
            func =getattr(self,function_str)
            func(instructions)
        else:
            print("\033[31;1mReceived invalid instruction [%s] from client" %instructions)
     #@login_required
    # def file_get(self,user_data):
    #     print("\033[32;1m---client get file---\033[0m")
    #     if self.login_user:
    #         filename_with_path = json.loads(user_data[1])
    #         #file_abs_path = "%s/%s/%s" %(settings.USER_HOME,self.login_user,filename_with_path)
    #         #print(file_abs_path)
    #         #if os.path.isfile(file_abs_path):
    #         #    file_size = os.path.getsize(file_abs_path)
    #             response_msg = "response|300|%s|n/a" %file_size
    #             self.request.send(response_msg)
    #             client_response = self.request.recv(1024).split("|")
    #             print('-->',client_response)
    #             if client_response[1] == "301":
    #                 sent_size = 0
    #          #       f = open(file_abs_path,"rb")
    #                 file_md5 = hashlib.md5()
    #                 t_start = time.time()
    #          #       while file_size != sent_size:
    #                     data = f.read(4096)
    #                     self.request.send(data)
    #                     sent_size += len(data)
    #                     print ("send:",file_size,sent_size)
    #                 else:
    #                     md5_str = file_md5.hexdigest()
    #                     t_cost = time.time() - t_start
    #                     print ("---file transfer time:---",t_cost)
    #                     print ("\033[32;1m---successfully sent file---")
    #                     f.close()
    #
    #             else:
    #                 response_msg = "response|302|n/a|n/a"
    #                 self.request.send(response_msg)
    #
    #
    # def user_auth(self,data):
    #     auth_info = json.loads(data[1])
    #     auth_info['username']
    #     auth_info['password']
    #     if auth_info['username'] in settings.USER_ACCOUNT:
    #         if settings.USER_ACCOUNT[auth_info['username']['password']]:
    #             response_code = '200'
    #             self.login_user = auth_info['username']
    #
    #         else:
    #             response_code = '201'
    #     else:
    #         response_code = '202'
    #     response_str = "response|%s|%s" %(response_code,)
    #     self.request.send(response_str)
    #     return response_code
    #


if __name__ == '__main__':
    pass




