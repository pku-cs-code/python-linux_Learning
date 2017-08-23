#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add_node(tree_dic,comment):
    if comment.parent_comment is None:
        #如果父评论为空，那么就放在这儿
        tree_dic[comment] = {}
    else:#如果不是，那么循环当前整个字典，直到找到为止
        for k,v in tree_dic.items():
            if k == comment.parent_comment:#找到了
                print('找到了dad--》',k)
                tree_dic[comment.parent_comment][comment] = {}
            else:#进入下一层继续中
                print('keeping going deeper...')
                add_node(v,comment)

        # tree_dic[comment.parent_comment][comment] = {}

        pass

def render_tree_node(tree_dic,margin_val):
    html = ""
    for k,v in tree_dic.items():
        ele = "<div class='comment-node'  style='margin-left:%spx'>" % margin_val + k.comment+ "<span style='margin-left:20px'>%s</span>" % k.date\
              + "<span style='margin-left:20px'>%s</span>" % k.user.name + \
              '<span comment-id="%s"'%k.id+'style="margin-left:20px"class="glyphicon glyphicon-comment add-comment" aria-hidden="true"></span>' + \
 \
              "</div>"
        html += ele
        html += render_tree_node(v,margin_val+16)
    return html

def render_comment_tree(tree_dic):
    html = ""
    for k,v in tree_dic.items():
        ele = "<div class='root-comment'>" + k.comment + "<span style='margin-left:20px'>%s</span>" % k.date\
              + "<span style='margin-left:20px'>%s</span>" % k.user.name + \
               '<span comment-id="%s"'%k.id+'style="margin-left:20px"class="glyphicon glyphicon-comment add-comment" aria-hidden="true"></span>' + \
              "</div>"
        html += ele
        html += render_tree_node(v,10)

    return html


def build_tree(comment_set):
    #print(comment_set)
    tree_dic = {}
    for comment in comment_set:
        add_node(tree_dic,comment)
    print('------')
    for k,v in tree_dic.items():
        print(k,v)

        pass
    return tree_dic