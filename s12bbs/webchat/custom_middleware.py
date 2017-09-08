#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyCustomMiddleware(object):
    def process_request(self, request):
        print("---in process request--")

    def process_view(self,request, view_func, view_args, view_kwargs):
        print("----in process view----")
        print(request, view_func, view_args, view_kwargs)

    def process_response(self,request, response):
        print("-----in process response----",response)
        return response

    def process_exception(self,request, exception):
        print("----coming ot exception---",exception)

