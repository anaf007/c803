#coding=utf-8

from environs import Env
env = Env()

#版本号
try:
	dev_1 = env.str('API_VERSION')
except Exception as e:
	dev_1 = 'v1'



