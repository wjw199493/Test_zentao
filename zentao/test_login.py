import unittest
import HTMLTestReportCN
from longin import Login
from excel_cz import Excel_dx
import requests
data = Excel_dx
longAPI = Login
s = requests.session()

class Test_longin(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.execute = data.bt(self,'是否执行')
        self.ststus_code = data.bt(self,'状态码')
        self.result = data.bt(self,'返回结果')
        self.ID = data.bt(self,'ID')
        self.host = data.bt(self,'API地址')
        self.data1 = data.bt(self,'请求参数')

    def test_001(self):
        u'''用户名为空码正确登陆'''
        h = int(data.du(self, 1, self.ID))#获取执行的行
        ss = eval(data.du(self, h, self.data1))  # 读取参数并转换为字典
        print(ss)
        host = (data.du(self, h, self.host))#获取url
        a ,b= longAPI.login(self, ss, host)#接收返回结果和状态吗
        print (a.decode('utf-8'))
        vale = a.decode('utf-8')
        data.xg(self, h, self.ststus_code, b)#写入状态码
        data.xg(self, h, self.result, vale)  # 写入返回结果
        data.xg(self, h, self.execute, "是")  # 写入执行状态
        print(longAPI.is_login(a.decode('utf-8'), h))

    def test_002(self):
        u'''用户名为空码正确登陆'''
        h = int(data.du(self, 2, self.ID))
        ss = eval(data.du(self,h, self.data1))  # 读取参数并转换为字典
        print (ss)
        host = (data.du(self,h, self.host))
        a ,b = longAPI.login(self,ss, host)
        print (a.decode('utf-8'))
        vale = a.decode('utf-8')
        data.xg(self, h, self.ststus_code, b)
        data.xg(self,h, self.result, vale)  # 写入返回结果
        data.xg(self, h, self.execute, "是")  # 写入执行状态
        print(longAPI.is_login(a.decode('utf-8'),h))

    def test_003(self):
        u'''用户名正确密码为空登陆'''
        h = int(data.du(self, 3, self.ID))
        ss = eval(data.du(self, h, self.data1))  # 读取参数并转换为字典
        print(ss)
        host = (data.du(self, h, self.host))
        a ,b = longAPI.login(self, ss, host)
        print (a.decode('utf-8'))
        vale = a.decode('utf-8')
        data.xg(self, h, self.ststus_code, b)
        data.xg(self, h, self.result, vale)  # 写入返回结果
        data.xg(self, h, self.execute, "是")  # 写入执行状态
        print(longAPI.is_login(a.decode('utf-8'), h))

    def test_004(self):
        u'''用户名密码均为空登陆'''
        h = int(data.du(self, 4, self.ID))
        ss = eval(data.du(self, h, self.data1))  # 读取参数并转换为字典
        print(ss)
        host = (data.du(self, h, self.host))
        a , b = longAPI.login(self, ss, host)
        print (a.decode('utf-8'))
        vale = a.decode('utf-8')
        data.xg(self, h, self.ststus_code, b)
        data.xg(self, h, self.result, vale)  # 写入返回结果
        data.xg(self, h, self.execute, "是")  # 写入执行状态
        print(longAPI.is_login(a.decode('utf-8'), h))

    def test_005(self):
        u'''用户名错误码正确登陆'''
        h = int(data.du(self, 5, self.ID))
        ss = eval(data.du(self,h, self.data1))  # 读取参数并转换为字典
        print (ss)
        host = (data.du(self,h, self.host))
        a ,b = longAPI.login(self,ss, host)
        print (a.decode('utf-8'))
        vale = a.decode('utf-8')
        data.xg(self, h, self.ststus_code, b)
        data.xg(self,h, self.result, vale)  # 写入返回结果
        data.xg(self, h, self.execute, "是")  # 写入执行状态
        print(longAPI.is_login(a.decode('utf-8'),h))

    def test_006(self):
        u'''用户名正确密码错误'''
        h = int(data.du(self, 6, self.ID))
        ss = eval(data.du(self, h, self.data1))  # 读取参数并转换为字典
        print(ss)
        host = (data.du(self, h, self.host))
        a ,b = longAPI.login(self, ss, host)
        print (a.decode('utf-8'))
        vale = a.decode('utf-8')
        data.xg(self, h, self.ststus_code, b)
        data.xg(self, h, self.result, vale)  # 写入返回结果
        data.xg(self, h, self.execute, "是")  # 写入执行状态
        print(longAPI.is_login(a.decode('utf-8'), h))

    def test_007(self):
        u'''用户名密码均错误'''
        h = int(data.du(self, 7, self.ID))
        ss = eval(data.du(self,h, self.data1))  # 读取参数并转换为字典
        print(ss)
        host = (data.du(self, h, self.host))
        a ,b = longAPI.login(self, ss, host)
        print (a.decode('utf-8'))
        vale = a.decode('utf-8')
        data.xg(self, h, self.ststus_code, b)
        data.xg(self, h, self.result, vale)  # 写入返回结果
        data.xg(self, h, self.execute, "是")  # 写入执行状态
        print(longAPI.is_login(a.decode('utf-8'), h))

    def test_008(self):
        u'''用户名缺失'''
        h = int(data.du(self, 8, self.ID))
        ss = eval(data.du(self,h, self.data1))  # 读取参数并转换为字典
        print(ss)
        host = (data.du(self, h, self.host))
        a ,b = longAPI.login(self, ss, host)
        print (a.decode('utf-8'))
        vale = a.decode('utf-8')
        data.xg(self, h, self.ststus_code, b)
        data.xg(self, h, self.result, vale)  # 写入返回结果
        data.xg(self, h, self.execute, "是")  # 写入执行状态
        print(longAPI.is_login(a.decode('utf-8'), h))

    def test_009(self):
        u'''密码缺失'''
        h = int(data.du(self,9, self.ID))
        ss = eval(data.du(self,h, self.data1))  # 读取参数并转换为字典
        print(ss)
        host = (data.du(self, h, self.host))
        a ,b = longAPI.login(self, ss, host)
        print (a.decode('utf-8'))
        vale = a.decode('utf-8')
        data.xg(self, h, self.ststus_code, b)
        data.xg(self, h, self.result, vale)  # 写入返回结果
        data.xg(self, h, self.execute, "是")  # 写入执行状态
        print(longAPI.is_login(a.decode('utf-8'), h))

    def test_0010(self):
        u'''账号和密码参数缺失'''
        h = int(data.du(self,10, self.ID))
        ss = eval(data.du(self,h, self.data1))  # 读取参数并转换为字典
        print(ss)
        host = (data.du(self, h, self.host))
        a ,b = longAPI.login(self, ss, host)
        print (a.decode('utf-8'))
        vale = a.decode('utf-8')
        data.xg(self, h, self.ststus_code, b)
        data.xg(self, h, self.result, vale)  # 写入返回结果
        data.xg(self, h, self.execute, "是")  # 写入执行状态
        print(longAPI.is_login(a.decode('utf-8'), h))

if __name__=="__main__":
    #生成测试报告
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test_longin)
    # suite = unittest.TestSuite([suite1])
    # print (suite)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    # suite = unittest.TestLoader().loadTestsFromTestCase(New_user)
    report = r'F:\untitled\我的坚果云\练习\zentao\登陆接口测试报告.html'
    fq = open(report, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fq,
                                             title=u'登陆接口测试报告',
                                             description=u'用例执行情况')
    runner.run(suite1)
    #发送电子邮件
    theme = '禅道登陆接口测试报告'
    main_body = '测试详情请查看附件'
    path = r'F:\untitled\我的坚果云\练习\zentao\登陆接口测试报告.html'
    recipients = '17139061609@163.com'+';'+'2579188890@qq.com'#收件人，多个收件人时用；隔开
    #copy_to = '2209309573@qq.com'#抄送对象，多个抄送对象时用；隔开
    copy_to = ' '#没有抄送对象时用空表示
    print (recipients)

    #mail.send_emain( recipients,copy_to, theme, main_body, path)