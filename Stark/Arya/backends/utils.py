#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Arya import action_list
import django
#django.setup()#加载app再导入models

from Stark import settings
from Arya import models#在前面两句话之后


class ArgvManagement(object):
    '''
    接收用户指令并分配到相应模块
    '''
    #print('导入ArgvManagement模块测试')

    def __init__(self,argvs):
        self.argvs = argvs
        self.argv_parse()

    def help_msg(self):
        print("Available modules:")
        for registered_module in action_list.actions:
            print("%s" %registered_module)
        exit()

    def argv_parse(self):
        #print(self.argvs)

        if len(self.argvs) < 2:
            self.help_msg()
        module_name = self.argvs[1]

        if '.' in module_name:
            mod_name,mod_method = module_name.split('.')

            module_instance = action_list.actions.get(mod_name)
            if module_instance:#matched
                module_obj = module_instance(self.argvs,models,settings)#将action_list中的cmd和state传给此self?
                module_obj.process()

                if hasattr(module_obj,mod_method):
                    module_method_ob = getattr(module_obj,mod_method)
                    module_method_ob()#调用指定的指令
                #module_obj.process()#解析任务，然后发送到队列，取任务结果
                else:
                    exit("module [%s] has no method [%s].")%(mod_name,mod_method)

        else:
            exit("invalid module name argument")



