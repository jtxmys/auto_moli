import smtplib
from email.header import Header
from email.mime.text import MIMEText


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['from'] = "bwftest126@126.com"
    msg['to'] = "changchengxc@126.com"

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("bwftest126@126.com", "abc123asd654")
    smtp.sendmail("bwftest126@126.com", "aaaaaayaojunchao@163.com", msg.as_string())
    smtp.quit()
    print('email has send out !')
if __name__ == '__main__':
    send_mail(r'C:\Users\lenovo\Desktop\aa.jpg')