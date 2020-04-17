import requests
import json

class RunMethod:
	def post_main(self,url,data,header=None):
		res = None
		try:
			if header !=None:
				if header['Content-Type'] =='application/x-www-form-urlencoded':
					res = requests.post(url=url,data=data,headers=header)
				else:
					res = requests.post(url=url,data=json.dumps(data),headers=header)
			else:
				res = requests.post(url=url,data=json.dumps(data))
			return res
		except Exception as ex_results:
			print("程序终止,抓了一个异常：",ex_results,)

	def get_main(self,url,data=None,header=None):
		res = None
		try:
			if header !=None:	
				res = requests.get(url=url,data=json.dumps(data),headers=header,verify=False)
			else:
				res = requests.get(url=url,data=json.dumps(data),verify=False)
			return res
		except Exception as ex_results:
			print("程序终止,抓了一个异常：",ex_results,)

	def run_main(self,url,method,header=None,data=None):
		res = None
		if method == 'POST':	
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		return res

    