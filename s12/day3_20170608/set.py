#!/usr/bin/env python

# l1 = []
# l2 = list()

# s1 =set()
# s1.add("alex")
# print(s1)
# s1.add("alex")
# print(s1)

# s2 = set(['alex','eric','tony','alex'])
# print(s2)
# s3 = s2.difference(['alex','eric'])
# print(s2)
# print(s3)
# s4 = s2.difference_update(['alex','eric'])
# print(s2)
# print(s4)
# ret = s2.pop()
# print(s2)
# print(ret)
# print (s2.remove('tony'))
# print(s2)

# s1 = set([11,22,33])
# s2 = set([22,44])
# ret1 = s1.difference(s2)
# ret2 = s1.symmetric_difference(s2)
# print(ret1)
# print(ret2)

# import collections
# obj = collections.Counter('ssfdffjkjk11;')
# print(obj)
# ret = obj.most_common(4)
# print(ret)
#
# for k in obj.elements():
#     #print(item)
#     print(k)
# for k,v in obj.items():
#     print(k,v)

# import collections
# obj = collections.Counter(['11','22','22','33'])
# print(obj)
# # obj.update(['eric','11','11'])
# # print(obj)
# obj.subtract(['eric','11','11'])
# print(obj)

# import collections
# dic =collections.OrderedDict()
# #dic = dict()
# dic['k1'] = 'v1'
# dic['k2'] = 'v2'
# dic['k3'] = 'v3'
#dic['k4'] = None
#dic.setdefault('k4','66')
# print(dic)
#
# dic.move_to_end('k1')
# print(dic)
# print(dic)
# #dic.popitem()
# ret = dic.pop('k2')
# print(dic)

# dic.update({'k1':'v111','k10':'v10'})
# print(dic)

# import collections
# MytupleClass = collections.namedtuple('MytupleClass',['x','y','z'])
# print(help(MytupleClass))
# obj = MytupleClass(11,22,33)
# print(obj.x)
# print(obj.y)
# print(obj.z)

# d = collections.deque()
# d.append('1')
# d.appendleft('10')
# d.appendleft('1')
# print(d)
#
# r = d.count('1')
# print(r)
# d.extend(['yy','uu','ii'])
# print(d)
#
# d.extendleft(['yly','ulu','ili'])
# print(d)
# d.rotate(3)
# print(d)

# import queue
# q = queue.Queue()
# q.put('123')
# q.put('678')
# print(q.qsize())
# print(q.get())

#import copy
# #浅拷贝
# copy.copy()
# #深拷贝
# copy.deepcopy()
# #赋值


#a1 = 123123
# # a2 = 123123
# a2 = a1
# print(id(a1),id(a2))

# a3 = copy.copy(a1)
# print(id(a1),id(a3))
# a3 = copy.deepcopy(a1)
# print(id(a1),id(a3))

#其他，元组、列表、字典
# n1 = {"k1":"wu","k2":123,"k3":{"alex",456}}
# n2 = n1
# print(id(n1),id(n2))

# n1 = {"k1":"wu","k2":123,"k3":{"alex",456}}
# n3 = copy.copy(n1)
# print(id(n1),id(n3))
#
# print(id(n1['k3']),id(n3['k3']))

# import copy
# n1 = {"k1":"wu","k2":123,"k3":{"alex",456}}
# n3 = copy.deepcopy(n1)
# print(id(n1),id(n3))
#
# print(id(n1['k3']),id(n3['k3']))

# import copy
# dic = {
#     "cpu":[80,],
#     "men":[80,],
#     "disk":[80,]
# }
# print(dic)
# new_dic = copy.copy(dic)
# new_dic['cpu'][0] = 50
# print(dic)

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail(user):
    ret = True
    try:
        msg = MIMEText('邮件内容','plain','utf-8')
        msg['From'] = formataddr(["张才",'xzhangcainginx@163.com'])
        msg['To'] = formataddr(["张才",'41422002x@qq.com'])
        msg['Subject'] = "主题"
        server = smtplib.SMTP("smtp.163.com",25)
        server.login("xzhangcainginx@163.com","邮箱密码")
        server.sendmail('xzhangcainginx@163.com',[user,],msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret

ret = mail('41422002x@qq.com')

#print(ret)
if ret:
    print("发送成功")
else:
    print("发送失败")

"""
def show():
    print('a')
    if 1 == 1:
        return [11,22]
    print('b')

ret = show()
print(ret)
"""

