#!/usr/bin/env python

import re

def deal_minus_issue(calc_list):
    new_calc_list = []
    for index,item in enumerate(calc_list):
        if item.strip().endswith("*") or item.strip().endswith("/"):
            new_calc_list.append("%s-%s" %(calc_list[index], calc_list[index+1]))
        elif "*" in item or "/" in item:
            new_calc_list.append(item)
    print("new_calc_list",new_calc_list)


def mutiply_and_dividend(formula):
    print("运算",formula)
    calc_list = re.split("[+-]",formula)
    calc_list = deal_minus_issue(calc_list)
    print(calc_list)
    for item in calc_list:
        sub_calc_list = re.split("[*/]",item)
        sub_operator_list = re.findall("[*/]",item)
        print(sub_calc_list,sub_operator_list)
        sub_res = None
        for index,i in enumerate(sub_calc_list):
            if sub_res:#这不是第一次循环
                if sub_operator_list[index-1] == "*":
                    sub_res *= float(i)
                else:
                    sub_res /= float(i)
            else:
                sub_res = float(i)
        print("\033[31;1m[%s]=\033[0m" %item,sub_res)
        #formula = re.sub(item,str(sub_res),formula)
        formula=formula.replace(item,str(sub_res),formula)

    print("\033[31;1m[%s]结果\033[0m" %formula)

def calc(formula):
    parentheses_flag = True
    while parentheses_flag:
        m = re.search("\([^()]+\)",formula)  #[^()]+一个或者多个
        if m:
            print(m.group())
            sub_formula = m.group().strip("()")
            sub_res = mutiply_and_dividend(sub_formula)
        break

if __name__ == "__main__":
    formula ="1 -2 * ((60 - 30 +  (9-2*5/3+7/3*99/4*2998+10*568/14)*(-40/5))-(-4*3)/(16-3*2))"
    res = calc(formula)
