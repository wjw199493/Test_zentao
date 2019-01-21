from nwe_user.test_newuser import Test_user
import HTMLTestReportCN
import unittest
from comm.report_email import Email
from longin.test_login import Test_longin
#longAPI = Login
mail = Email
suite = unittest.TestLoader().loadTestsFromTestCase(Test_user)
suite1 = unittest.TestLoader().loadTestsFromTestCase(Test_longin)
report = './comm/创建用户测试报告.html'
fq = open(report, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fq,
                                         title=u'创建用户测试报告',
                                         description=u'用例执行情况')
runner.run(suite)
report = './comm登陆接口测试报告.html'
fq = open(report, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fq,
                                         title=u'创建用户测试报告',
                                         description=u'用例执行情况')
runner.run(suite1)
theme = '禅道新建用户接口测试报告'
main_body = '测试详情请查看附件'
path = ['./comm/登陆接口测试报告.html','./comm/创建用户测试报告.html']
recipients = '1427464220@qq.com,2209309573@qq.com'#收件人，多个收件人时用；隔开
#copy_to = '2209309573@qq.com'#抄送对象，多个抄送对象时用；隔开
copy_to = ' '#没有抄送对象时用空表示
mail.send(path, recipients, copy_to, theme,main_body )
