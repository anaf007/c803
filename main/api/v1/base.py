#coding=utf-8

from flask_restful import Resource
from main.extensions import api
from main.public.models import Product
from flask import request

from pprint import pprint

from .version import dev_1
v1 = dev_1

class Info(Resource):

	def get(self):
		try:
			res = Product.query.all()
			temp = []
			for x in res:
				temp.append(x.to_json())

			return {'res':temp}

		except Exception as e:
			
			return {'msg':'null data,error:'+str(e)},401
		


api.add_resource(Info, f'/api/{v1}/base/info')  


    


