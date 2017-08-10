#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,socket,json

class Client(object):

    def __init__(self, sys_argv):
        self.args = sys_argv
        self.argv_parser()
        self.response_code ={
            "200":"pass user authentication",
            "201":"wrong username or password",
            "202":"invalid username or password",

        }
        self.handle()

    def help_msg(self):
        msg ='''
        -s ftp_server_addr    :ftp server ip address
        -p ftp_server_port    :ftp server port
        '''
        print (msg)

    def instruction_msg(self):
        msg = """
        get ftp_file :download file from ftp server
        put local remote: upload file to remote server
        ls:  list file
        cd path: change dir on ftp server
        """

    def argv_parser(self):
        if len(self.args) < 5:
            self.help_msg()
            sys.exit()

        else:
            mandatory_fields = ["-p","-s"]
            for i in mandatory_fields:
                if i not in self.args:
                    sys.exit("\033[31;1mLack of argument [%s] \033[0m")
            try:
                self.ftp_host = self.args[self.args.index("-s")]
                self.ftp_port = int(self.args[self.args.index])
            except (IndexError,ValueError):
                self.help_msg()
                self.exit()

    def connect(self,host,port):
        try:
            self.sock = socket.socket(socket.AF_INET,socket.SO_ACCEPTCONN)
            self.sock.connect((host,port))
        except socket.error as e:
            sys.exit("\033[31;1m%s\033[0m"%e)

    def auth(self):
        retry_count = 0
        while retry_count < 3:
            username = raw_input("\033[32;1mUsername:\033[0m")
            if len(username) == 0:continue
            password = raw_input("\033[32;1mPassword:\033[0m")
            if len(password) == 0:continue
            raw_json = json.dumps({
                'username':username,
                'password':password,
            })
            auth_str = "user_auth|%s" %raw_json
            self.sock.send(auth_str)
            server_response = self.sock.recv(1024)
            response_code = self.get_response_code(server_response)
            print (self.response_code[response_code])
            if response_code == '200':
                self.login_user = username
                self.cwd = "/"
                return True



