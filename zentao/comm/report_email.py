import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import  make_header
class Email():
    def send(self,xx,receiver,copy_to,mail_title,text_part):
        sender = 'xxxxxx@qq.com'
        receiver = receiver
        copy_to =  copy_to
        smtpserver = 'smtp.163.com'       #邮箱服务器，163邮箱为smtp.163.com，qq邮箱为smtp.qq.com，根据实际情况选择
        username = 'xxxxxx@163.com'  #邮箱账号
        # 如果是163邮箱，这里的密码是163的授权码而不是登陆密码。qq邮箱使用qq邮箱生成的授权吗。
        password = 'xxxxxx'
        mail_title = mail_title

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = sender  #发件人邮箱
        # message['To'] = receiver  #收件人邮箱，格式"xxxxx@163.com，xxxxx@qq.com"
        # print (receiver)
        message['To'] = ','.join(receiver ) #收件人邮箱，格式"xxxxx@163.com，xxxxx@qq.com"
        print ( ','.join(receiver ))
        message['Cc'] = ','.join(copy_to )   #邮件抄送对象，格式"xxxxx@163.com，xxxxx@qq.com"
        message['Subject'] = Header(mail_title, 'utf-8')
        message.attach(MIMEText(text_part, 'plain', 'utf-8'))

        att = []
        #通过循环统计附件个数，便于添加添加附件
        for j in range(len(xx)):
            att.append(j)
        #通过for循环添加附件，这里的xx表示附件路径，xx为list
        for i in range(len(xx)):#
            print(xx[i-1].split("/")[-1])
            path_file = xx[i-1]   #获取列表中的单个文件路径
            file= xx[i-1].split("/")[-1]
            att[i]= MIMEText(open(path_file,'rb').read(),'base64','utf-8')
            att[i]["Content-Type"] = 'application/octet-stream;name="%s"' % make_header([(file, 'UTF-8')]).encode('UTF-8')#解决附件中文名乱码问题
            att[i]["Content-Disposition"] = 'attachment;filename= "%s"' % make_header([(file, 'UTF-8')]).encode('UTF-8')
            message.attach(att[i])

        try:
            smtpObj = smtplib.SMTP_SSL()  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
            smtpObj.connect(smtpserver)
            smtpObj.login(username, password)
            smtpObj.sendmail(sender, receiver+copy_to, message.as_string())#receiver+copy_to收件人和抄送对象需要放在同一列表中
            print("邮件发送成功！！！")
            smtpObj.quit()
        except:
            print ('邮件发送失败')
            smtpObj.quit()
if __name__ == '__main__':
    xx = ['C:/Users/lenve/Desktop/f708ce81f86372ef9b6436edb3801711.mp4','C:/Users/lenve/Desktop/git 初步使用教程.doc']
    receiver =['xxxxxx@163.com','xxxxxx@163.com']
    copy_to =  ['xxxxxx@qq.com','xxxxxx@qq.com']
    #copy_to = ''
    mail_title = '主题：发送，抄送多人'
    text_part = '测试多人发送，和多人接收'
    email = Email()
    email.send(xx,receiver,copy_to,mail_title,text_part)
