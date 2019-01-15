import requests
import time
from excel_cz import Excel_dx
from longin import Login
longAPI = Login
data_use = Excel_dx
rs = requests.session()
class New_user():

    def new_use(self,data,url,rs):
        r = rs.post(url = url,data = data)
        #print (r.content.decode('utf-8'))
        return r.content , r.status_code


    def is_new(self,res,h):
        assert1 = '这条记录了。如果您确定该记录已删除，请到后台管理-回收站还原'
        assert2 = '/zentao/user-login-L3plbnRhby91c2VyLWNyZWF0ZS0wLmh0bWw=.html'
        assert3 = '/zentao/company-browse.html'
        assert4 = '『密码』不能为空。'
        assert5 = '两次密码应当相等。'
        assert6 = '安全验证密码错误，请输入你的登录密码'
        assert7 = '用户名』不能为空。'
        assert8 = '『用户名』应当为合法的用户名'
        assert9 = '『真实姓名』不能为空。'
        assert10 = '密码应该符合规则，长度至少为六位。'
        assert11 = '添加用户 - 禅道'
        result = data_use.bt(self,'执行结果')
        ru_time = data_use.bt(self,'执行时间')

        if assert1 in res:
            print (assert1)
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self,h, result, assert1)
            data_use.xg(self,h, ru_time, run_time)
        elif assert2 in res:
            print ('已退出登陆，正在重新登陆......')
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self,h, result, assert3)
            data_use.xg(self,h, ru_time, run_time)
        elif  assert3 in res:
            print('添加成功')
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self,h, result, assert3)
            data_use.xg(self,h, ru_time, run_time)
        elif  assert4 in res:
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self,h, result, assert4)
            data_use.xg(self,h, ru_time, run_time)
            print (assert4)
        elif assert5 in res:
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self,h, result, assert5)
            data_use.xg(self,h, ru_time, run_time)
            print (assert5)
        elif assert6 in res:
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self,h, result, assert6)
            data_use.xg(self,h, ru_time, run_time)
            print (assert6)
        elif assert7 in res:
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self,h, result, assert7)
            data_use.xg(self,h, ru_time, run_time)
            print (assert7)
        elif  assert8 in res:
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self,h, result, assert8)
            data_use.xg(self,h, ru_time, run_time)
            print (assert8)
        elif  assert9 in res:
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self,h, result,assert9)
            data_use.xg(self,h, ru_time, run_time)
            print ( assert9)
        elif  assert10 in res:
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self,h, result,assert9)
            data_use.xg(self,h, ru_time, run_time)
            print ( assert10)
        elif  assert11 in res:
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self,h, result,'所有参数缺失')
            data_use.xg(self,h, ru_time, run_time)
            print ('所有参数缺失')


        else:
            print('Flase')
            run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data_use.xg(self, h, result, 'Flase')
            data_use.xg(self, h, ru_time, run_time)
# class New_user():
#     def user(self):
if __name__ ==  '__main__':
    aa = New_user
    self = 1
    a = aa.new_use(self)


