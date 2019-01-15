import requests
import unittest
import HTMLTestReportCN
from excel_cz import Excel_dx
from longin import Login
from new_user import New_user
from emain import Email_new
mail = Email_new
Newuser = New_user
longAPI = Login
data_user = Excel_dx
rs = requests.session()

class Test_user(unittest.TestCase):
    @classmethod
    def setUpClass(self):#setUpClasss和taerDownClass使用时前面要加@classmethod
        self.execute = data_user.bt(self, '是否执行')
        self.ststus_code = data_user.bt(self, '状态码')
        self.result = data_user.bt(self, '返回结果')
        self.ID = data_user.bt(self, 'ID')
        self.host = data_user.bt(self, 'API地址')
        self.data = data_user.bt(self, '请求参数')
        h = int(data_user.du(self, 1, self.ID))
        host = (data_user.du(self, h, self.host))
        ss = eval(data_user.du(self, h, self.data))
        r = rs.post(url=host, data=ss)
        if 'http://127.0.0.1/zentao/my/' in str(r.content):
            print('已成功登陆')
        else:
            print('登陆失败')

    def test_0011(self):
        h = int(data_user.du(self, 11, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        #print(ss)
        host = (data_user.du(self, h, self.host))
        a ,b = Newuser.new_use(self,data_use,host,rs)
        vale = a.decode('utf-8')
        print (vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'),h)

    def test_0012(self):
        u'''用户名为空'''
        h = int(data_user.du(self, 12, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        #print(ss)
        host = (data_user.du(self, h, self.host))
        a ,b = Newuser.new_use(self,data_use,host,rs)
        vale = a.decode('utf-8')
        print (vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'),h)

    def test_0013(self):
        u'''真实姓名为空'''
        h = int(data_user.du(self, 13, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        #print(ss)
        host = (data_user.du(self, h, self.host))
        a ,b = Newuser.new_use(self,data_use,host,rs)
        vale = a.decode('utf-8')
        print (vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'),h)

    def test_0014(self):
        u'''密码为空'''
        h = int(data_user.du(self, 14, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        #print(ss)
        host = (data_user.du(self, h, self.host))
        a ,b = Newuser.new_use(self,data_use,host,rs)
        vale = a.decode('utf-8')
        print (vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'),h)

    def test_0015(self):
        u'''确认密码为空'''
        h = int(data_user.du(self, 15, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        #print(ss)
        host = (data_user.du(self, h, self.host))
        a ,b = Newuser.new_use(self,data_use,host,rs)
        vale = a.decode('utf-8')
        print (vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'),h)

    def test_0016(self):
        u'''安全验证密码为空'''
        h = int(data_user.du(self, 16, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        #print(ss)
        host = (data_user.du(self, h, self.host))
        a ,b = Newuser.new_use(self,data_use,host,rs)
        vale = a.decode('utf-8')
        print (vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'),h)

    def test_0017(self):
        u'''密码和确认密码不一致'''
        h = int(data_user.du(self, 17, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        #print(ss)
        host = (data_user.du(self, h, self.host))
        a ,b = Newuser.new_use(self,data_use,host,rs)
        vale = a.decode('utf-8')
        print (vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'),h)

    def test_0018(self):
        u'''密码错误'''
        h = int(data_user.du(self, 18, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        #print(ss)
        host = (data_user.du(self, h, self.host))
        a ,b = Newuser.new_use(self,data_use,host,rs)
        vale = a.decode('utf-8')
        print (vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'),h)
    def test_0019(self):
        u'''安全验证密码长度不够'''
        h = int(data_user.du(self, 19, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        #print(ss)
        host = (data_user.du(self, h, self.host))
        a ,b = Newuser.new_use(self,data_use,host,rs)
        vale = a.decode('utf-8')
        print (vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'),h)
    def test_0020(self):
        u'''安全验证密码与管理员密码不一致'''
        h = int(data_user.du(self, 20, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        #print(ss)
        host = (data_user.du(self, h, self.host))
        a ,b = Newuser.new_use(self,data_use,host,rs)
        vale = a.decode('utf-8')
        print (vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'),h)
    def test_0021(self):
        u'''用户名缺失'''
        h = int(data_user.du(self, 21, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        #print(ss)
        host = (data_user.du(self, h, self.host))
        a ,b = Newuser.new_use(self,data_use,host,rs)
        vale = a.decode('utf-8')
        print (vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'),h)

    def test_0022(self):
        u'''用户名缺失'''
        h = int(data_user.du(self, 22, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        # print(ss)
        host = (data_user.du(self, h, self.host))
        a, b = Newuser.new_use(self, data_use, host, rs)
        vale = a.decode('utf-8')
        print(vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'), h)

    def test_0023(self):
        u'''密码缺失'''
        h = int(data_user.du(self, 23, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        # print(ss)
        host = (data_user.du(self, h, self.host))
        a, b = Newuser.new_use(self, data_use, host, rs)
        vale = a.decode('utf-8')
        print(vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'), h)

    def test_0024(self):
        u'''确认密码缺失'''
        h = int(data_user.du(self, 24, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        # print(ss)
        host = (data_user.du(self, h, self.host))
        a, b = Newuser.new_use(self, data_use, host, rs)
        vale = a.decode('utf-8')
        print(vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'), h)

    def test_0025(self):
        u'''安全验证密码缺失'''
        h = int(data_user.du(self, 25, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        # print(ss)
        host = (data_user.du(self, h, self.host))
        a, b = Newuser.new_use(self, data_use, host, rs)
        vale = a.decode('utf-8')
        print(vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'), h)

    # def test_0026(self):
    #     u'''所有阐述缺失'''
    #     h = int(data_user.du(self, 26, self.ID))
    #     data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
    #     # print(ss)
    #     host = (data_user.du(self, h, self.host))
    #     a, b = Newuser.new_use(self, data_use, host, rs)
    #     vale = a.decode('utf-8')
    #     print(vale)
    #     data_user.xg(self, h, self.ststus_code, b)
    #     data_user.xg(self, h, self.result, vale)  # 写入返回结果
    #     data_user.xg(self, h, self.execute, "是")  # 写入执行状态
    #     Newuser.is_new(self, a.decode('utf-8'), h)

    def test_0027(self):
        u'''添加已存在用户'''
        h = int(data_user.du(self, 27, self.ID))
        data_use = eval(data_user.du(self, h, self.data))  # 读取参数并转换为字典
        # print(ss)
        host = (data_user.du(self, h, self.host))
        a, b = Newuser.new_use(self, data_use, host, rs)
        vale = a.decode('utf-8')
        print(vale)
        data_user.xg(self, h, self.ststus_code, b)
        data_user.xg(self, h, self.result, vale)  # 写入返回结果
        data_user.xg(self, h, self.execute, "是")  # 写入执行状态
        Newuser.is_new(self, a.decode('utf-8'), h)




if __name__ == "__main__":
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Test_user)
    # suite = unittest.TestSuite([suite1])
    # unittest.TextTestRunner(verbosity = 1).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_user)
    report = r'F:\untitled\我的坚果云\练习\zentao\创建用户测试报告.html'
    fq = open(report, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fq,
                                             title=u'创建用户测试报告',
                                             description=u'用例执行情况')
    runner.run(suite)
    theme = '禅道新建用户接口测试报告'
    main_body = '测试详情请查看附件'
    path = r'F:\untitled\我的坚果云\练习\zentao\创建用户测试报告.html'
    recipients = '17139061609@163.com'+';'+'2579188890@qq.com'#收件人，多个收件人时用；隔开
    #copy_to = '2209309573@qq.com'#抄送对象，多个抄送对象时用；隔开
    copy_to = ' '#没有抄送对象时用空表示
    print (recipients)

    mail.send_emain( recipients,copy_to, theme, main_body, path)