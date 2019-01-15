import win32com.client as win32
import xlrd
class Email_new():
    def send_emain(recipients,copy_to,theme,main_body,path):
        #print (1)
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        receivers = recipients
        mail.To = receivers#收件人
        mail.CC = copy_to#抄送对象
        mail.Subject = theme#主题
        mail.Body = main_body#正文
        mail.Attachments.Add(path)#附件路径
        mail.Send()
        print('发送成功')
    def ss(self):
        print(1)

if __name__ =='__main__':
    theme = '禅道创建用户接口测试报告测试发送邮件'
    main_body = '禅道创建用户接口测试请情况详情请查附件'
    path = r'F:\untitled\我的坚果云\练习\zentao\登陆接口测试报告.html'
    aa = Email_new()
    aa.send_emain(theme, main_body,path)

