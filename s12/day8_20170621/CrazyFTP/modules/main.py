#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,settings,threading_socket_server



class Argv(object):
    def __init__(self,args):
        self.args = args
        self.argv_parser()

    def argv_parser(self):
        if len(self.args) < 2:
            self.help_msg()
        else:
            first_argv = self.args[1]
            if hasattr(self,first_argv):
                func = getattr(self,first_argv)
                func()

            else:
                self.help_msg()

    def help_msg(self):
        msg = '''
        start  :start ftp server
        stop   ：stop ftp server
        
        '''
        print(msg)

    def start(self):
        server = threading_socket_server.SocketServer.ThreadingTCPServer((settings.BIND_HOST, settings.BIND_PORT),
                                                                         threading_socket_server.MyTCPHandler)
        try:

            server.serve_forever()
        except KeyboardInterrupt:
            print("-----going to shutdown ftp server------")
            server.shutdown()

