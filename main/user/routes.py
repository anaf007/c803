#coding=utf-8
from main.helpers import url

def reg_url(bp):
    """注册路由"""
    #home
    url(bp,'/', 'members')