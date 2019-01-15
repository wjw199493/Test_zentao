import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = '17139061609@163.com'
receiver = '1427464220@qq.com'
smtpserver = 'smtp.163.com'
username = '17139061609@163.com'
password = 'wjw17139061609'
mail_title = '主题：这是带附件的邮件'

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(mail_title, 'utf-8')

#as = [r'C:\Users\lenve\Desktop\test.txt',r'D:\应用软件\微信\微信下载\WeChat Files\wxid_xxm4b0j1yrm822\Image\Image\0b789d6881d7803797cee30dfbf7fe49.jpg']
message.attach(MIMEText('来来来，这是邮件的正hhhhhhhhhhhhhhhhhhhhhhhhhhhh文', 'plain', 'utf-8'))

# 邮件正文内容
    #message.attach(MIMEText('来来来，这是邮件的正文', 'plain', 'utf-8'))

# # 构造附件1（附件为TXT格式的文本）
#     aa = r'C:\Users\lenve\Desktop\test.txt'#文件路径
#     att1 = MIMEText(open(aa, 'rb').read(), 'base64', 'utf-8')
#     att1["Content-Type"] = 'application/octet-stream'
#     att1["Content-Disposition"] = 'attachment; filename="test.txt"'
#     message.attach(att1)
xx = [r'C:\Users\lenve\Desktop\dd.xlsx',r'C:\Users\lenve\Pictures\sunset.jpg']
att = [1,2,3,4,5,6,7]
for i in range(len(xx)):
    print (xx[i-1].split("\\")[-1])
    aa = xx[i]
    ab = xx[i-1].split("\\")[-1]
    bc = xx[i-1].split(".")[-1]
    att[i]= MIMEText(open(aa,'rb').read(),'base64','utf-8')
    att[i]["Content-Type"] = 'application/octet-stream'
    att[i]["Content-Disposition"] = 'attachment;filename=%s'%ab
    message.attach(att[i])

#  # 构造附件2（附件为JPG格式的图片）
# ab = r'D:\应用软件\微信\微信下载\WeChat Files\wxid_xxm4b0j1yrm822\Image\Image\0b789d6881d7803797cee30dfbf7fe49.jpg'
# att2 = MIMEText(open(ab, 'rb').read(), 'jpg', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="88.jpg"'
# message.attach(att2)
# #
# # 构造附件3（附件为HTML格式的网页）
# att3 = MIMEText(open('report_test.html', 'rb').read(), 'base64', 'utf-8')
# att3["Content-Type"] = 'application/octet-stream'
# att3["Content-Disposition"] = 'attachment; filename="report_test.html"'
# message.attach(att3)

smtpObj = smtplib.SMTP_SSL()  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
smtpObj.connect(smtpserver)
smtpObj.login(username, password)
smtpObj.sendmail(sender, receiver, message.as_string())
print("邮件发送成功！！！")
smtpObj.quit()