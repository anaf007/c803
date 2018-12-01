#coding=utf-8
from main.helpers import url

def reg_url(bp):
    """注册路由"""
    #管理员首页
    url(bp,'/', 'index')
    #管理员主页
    url(bp,'/home', 'home')
    #管理员登录
    url(bp,'/login', 'login',methods=['POST','GET'])
    #管理员退出
    url(bp,'/logout', 'logout')
    #注册会员
    url(bp,'/user_add', 'user_add',methods=['POST','GET'])
    #未激活会员
    url(bp,'/user_index', 'user_index')
    #正式会员
    url(bp,'/user_list', 'user_list')
    #推荐图
    url(bp,'/retree', 'retree')

    #货币变更
    url(bp,'/cash_monenychange', 'cash_monenychange')
    #货币明细列表
    url(bp,'/cash_list', 'cash_list')
    #货币转账记录
    url(bp,'/cash_transfer', 'cash_transfer')
    #货币提现记录
    url(bp,'/withcashlist', 'withcashlist')
    
    #货币提现记录
    url(bp,'/miner_list', 'miner_list')

    #系统设置
    url(bp,'/system_config', 'system_config')
    #奖金设置
    url(bp,'/bonus_config', 'bonus_config')

