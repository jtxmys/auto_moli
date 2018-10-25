#!/usr/bin/env python3
# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    # msg['from'] = "bwftest126@126.com"
    msg['from'] = "aaaaaayaojunchao@163.com"
    msg['to'] = "1322202044@qq.com"

    try:
        smtp = smtplib.SMTP()
        smtp.connect("smtp.163.com")
        smtp.login("bwftest126@126.com", "abc123asd654")
        smtp.login("aaaaaayaojunchao@163.com", "123456789")
        # smtp.sendmail("bwftest126@126.com", "changchengxc@126.com", msg.as_string())

        smtp.sendmail("bwftest126@126.com", "aaaaaayaojunchao@163.com", msg.as_string())
    except smtplib.SMTPAuthenticationError as e:
        print(e)
        print('发送失败，请检查邮箱授权码')

        smtp.quit()
        print('email has send out !')
    else:
        print('email has send out !')

        smtp.quit()

if __name__ == '__main__':
    send_mail(r'C:\Users\lenovo\Desktop\aa.jpg')