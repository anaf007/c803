#coding=utf-8
from main.helpers import url

def reg_url(bp):
    """注册路由"""
    #home
    url(bp,'/', 'home')
    #logout
    url(bp,'/logout/','logout')
    url(bp,'/register/','register')
    #about
    url(bp,'/about/','about')
    #login
    url(bp,'/login/','login',methods=['GET', 'POST'])

