import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import  make_header
class Email():
    def send(xx,receiver,copy_to,mail_title,text_part):
        sender = '17139061609@163.com'
        receiver = receiver
        copy_to =  copy_to
        smtpserver = 'smtp.163.com'
        username = '17139061609@163.com'
        password = 'wjw17139061609'
        mail_title = mail_title

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Cc'] = copy_to
        message['Subject'] = Header(mail_title, 'utf-8')

        #as = [r'C:\Users\lenve\Desktop\test.txt',r'D:\应用软件\微信\微信下载\WeChat Files\wxid_xxm4b0j1yrm822\Image\Image\0b789d6881d7803797cee30dfbf7fe49.jpg']
        message.attach(MIMEText(text_part, 'plain', 'utf-8'))

        #print (xx)
        att = []
        #通过循环统计附件个数便于添加添加附件
        for j in range(len(xx)):
            att.append(j)
        for i in range(len(xx)):#添加附件方法
            print(xx[i-1].split("/")[-1])
            path_file = xx[i-1]
            file= xx[i-1].split("/")[-1]
            att[i]= MIMEText(open(path_file,'rb').read(),'base64','utf-8')
            att[i]["Content-Type"] = 'application/octet-stream;name="%s"' % make_header([(file, 'UTF-8')]).encode('UTF-8')#解决附件中文名乱码问题
            att[i]["Content-Disposition"] = 'attachment;filename= "%s"' % make_header([(file, 'UTF-8')]).encode('UTF-8')
            message.attach(att[i])

        try:
            smtpObj = smtplib.SMTP_SSL()  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
            smtpObj.connect(smtpserver)
            smtpObj.login(username, password)
            smtpObj.sendmail(sender, receiver, message.as_string())
            print("邮件发送成功！！！")
            smtpObj.quit()
        except:
            print ('邮件发送失败')
            smtpObj.quit()
if __name__ == '__main__':
    xx = ['../comm/登陆接口测试报告.html']
    receiver = '1427464220@qq.com,2209309573@qq.com'
    #copy_to =  '2579188890@qq.com'
    copy_to = ''
    mail_title = '主题：这是带附件的邮件'
    text_part = '测试同时发送大多人，携带不同格式附件'
    email = Email()
    email.send(xx,receiver,copy_to,mail_title,text_part)
