import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '645279566@qq.com'  # 发件人邮箱账号
my_pass = 'lrsrkqyipqxvbcfi'  # 发件人邮箱密码
my_user = '645279566@qq.com'  # 收件人邮箱账号


def send_mail(mail_content, from_user='tScripts', to_user='老大', title='默认脚本邮件'):
    print("开始发送邮件..")
    try:
        msg = MIMEText(mail_content, 'plain', 'utf-8')
        msg['From'] = formataddr([from_user, my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([to_user, my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = title  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        print("邮件发送失败")
        return

    print("邮件发送成功")

if __name__ == "__main__":
    content = 'edfsdfdsfsd\nfsdfsdfsdfsd\nnn'
    send_mail(content)
