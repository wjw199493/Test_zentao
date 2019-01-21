from  comm.excel_cz import Excel_dx as data
import requests
import time

data =data()
ss = eval(data.du(1,9))#读取参数并转换为字典nn
host = (data.du(1,2))


import unittest
#s = requests.session()
#host = 'http://127.0.0.1'
class Login():
	def login(self,ss,host):
		#host = 'http://127.0.0.1'
		print (host)
		url = host #+'/zentao/user-login-L3plbnRhby8=.html '
		#s = requests.session() #不要写死
		# data = {'account':username,
        # 	'password':psw,
        # 	'referer':host+'/zentao/my/'}
		#print (data)
		header = {
			'Accept':'text/html, application/xhtml+xml, image/jxr, */*',
			'Referer':host+'/zentao/user-login-L3plbnRhby8=.html',
			'Accept-Language':'zh-CN',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
			'Content-Type':'application/x-www-form-urlencoded',
			'Accept-Encoding':'gzip, deflate',
			'Content-Length':'76',
			'DNT':'1',
			'Host':'127.0.0.1',
			'Connection':'Keep-Alive',
			'Pragma':'no-cache',

			#Cookie: lang=zh-cn; theme=default; windowWidth=1371; windowHeight=628; sid=mlmt4h2kcfe96727cqk2heluv1

		}
		r = requests.post(url= url,data = ss,headers = header)
		#print (r.content.decode('utf-8'))
		return r.content ,r.status_code

	def is_login(res,h):
		#res ==a.decode('utf-8')登陆接口返回的数据
		a0 = "parent.location='http://127.0.0.1/zentao/my/'"
		a1 = "登录失败，请检查您的用户名或密码是否填写正确。"
		a2 = '您还有3次尝试机会。'
		a3 = '您还有2次尝试机会。'
		a4 = '您还有1次尝试机会。'
		a5 = '密码尝试次数太多，请联系管理员解锁，或10分钟后重试。'
		result = data.bt('执行结果')
		ru_time = data.bt('执行时间')

		if  a0 or a1 or a2 or a3 or a4 in res:
			if a0 in res:
				vale = a0
				run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
				data.xg(h, result, vale)
				data.xg(h, ru_time, run_time)
				return True

			elif  a1 in res:
				vale = a1
				run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
				data.xg(h, result, vale)
				data.xg(h, ru_time, run_time)
				return True
			elif  a2 in res:
				vale = a2
				run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
				data.xg(h, result, vale)
				data.xg(h, ru_time, run_time)
				return True
			elif  a3 in res:
				vale = a3
				run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
				data.xg(h, result, vale)
				data.xg(h, ru_time, run_time)
				return True
			elif  a4 in res:
				vale = a4
				run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
				data.xg(h, result, vale)
				data.xg(h, ru_time, run_time)
				return True
			else:
				vale = a5
				run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
				data.xg(h, result, vale)
				data.xg(h, ru_time, run_time)
				return True

		else:
			vale = 'False'
			run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

			data.xg(h, result, vale)
			data.xg(h, ru_time, run_time)
			return False


if __name__=='__main__':
	self = 'pass'
	a ,b= Login.login(self,ss,host)
	print (a.decode('utf-8'))
	#print (a.status_code)
	vale = a.decode('utf-8')
	data.xg(1,11,vale)#写入返回结果
	print (Login.is_login(a.decode('utf-8'),1))
