#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseSaltModel(object):
    def __init__(self,sys_argvs,db_models,settings):
    # def __init__(self,sys_argvs):
        self.settings = settings
        self.sys_argvs = sys_argvs
        self.db_models = db_models
        self.fetch_hosts()
        self.config_data_dic = self.get_selected_os_types()

    def get_selected_os_types(self):
        data = {}
        for host in self.host_list:
            data[host.os_type] = []
        print('---->data',data)
        return data

    def process(self):
        pass

    def fetch_hosts(self):
        print('self.sys_argvs',self.sys_argvs)
        print('----fetching hosts-----')
        host_list = []

        if '-h' in self.sys_argvs or '-g' in self.sys_argvs:
            if '-h' in self.sys_argvs:
                host_str_index = self.sys_argvs.index('-h') + 1
                if len(self.sys_argvs) <= host_str_index:
                    exit("host arguement must be provided after -h")
                else:
                    host_str = self.sys_argvs[host_str_index]
                    host_str_list = host_str.split(',')
                    host_list += self.db_models.Host.objects.filter(hostname__in=host_str_list)
                    print("----host list----",host_list)
            # else:
            #     exit("host [-h] or group [-g]  arguement must be provided")

            if '-g' in self.sys_argvs:
                group_str_index = self.sys_argvs.index('-g') + 1
                if len(self.sys_argvs) <= group_str_index:
                    exit("host arguement must be provided after -h")
                else:
                    group_str = self.sys_argvs[group_str_index]
                    group_str_list = group_str.split(',')
                    group_list = self.db_models.HostGroup.objects.filter(name__in=group_str_list)
                    for group in group_list:
                        host_list += group.hosts.select_related()
            self.host_list = set(host_list)#去重
            return True
            print("----host list----",host_list)
        else:
            exit("host [-h] or group [-g]  arguement must be provided")


    def syntax_parser(self,section_name,mod_name,mod_data):
        print('systax_parser',section_name,mod_name,mod_data)
        for stat_item in mod_data:
            print("\t",stat_item)


