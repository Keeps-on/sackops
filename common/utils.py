from django.conf import settings
from django.core.mail import send_mail

############# 简单发送邮件 #############
# https://blog.csdn.net/BestFM/article/details/94065726
"""
    send_main(subject，message，from_email，recipient_list，fail_silently = False，auth_user = None，auth_password = None，connection = None，html_message = None)
    参数1：一个字符串，表示文件的主题
    参数2：一个字符串，邮件的内容
    参数3：一个字符串，发送者
    参数4：字符串列表，表示收件人
    参数5：为False时，send_mail()在发生错误时会抛出 smtplib.SMTPException异常
    参数6：可选的用户名用来验证SMTP服务器，如果你要特别指定使用哪个邮箱帐号，就指定这个参数。如果没有提供这个值，Django将会使用settings中EMAIL_HOST_USER的值
    参数7：可选的密码用来验证SMTP服务器。如果没有提供这个值，Django 将会使用settings中EMAIL_HOST_PASSWORD的值。
    参数8：可选的用来发送邮件的电子邮件后端
    参数9：如果提供了html_message，可以发送带HTML代码的邮件
"""


def send_mail_async(*args, **kwargs):
    subject = "邮件测试"
    message = "Django单人邮件发送测试"
    from_email = settings.EMAIL_FROM
    recipient_list = ['1299793997@qq.com', '564060577@qq.com']
    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
        auth_user=None,
        auth_password=None,
        connection=None,
        html_message=None,
    )


############# 多人发送邮件 #############
"""
    send_mass_mail(datatuple，fail_silently = False，auth_user = None，auth_password = None，connection = None)
    参数1：是一个元组，每个元组的类型为(subject，message，from_email，recipient_list)
    参数2：参数3：参数4：参数5：与send_mail()中的相同
"""
"""
    mail_admins（subject，message，fail_silently = False，connection = None，html_message = None）
    使用EMAIL_SUBJECT_PREFIX设置的值为邮件标题前缀，默认为'Django'
    使用SERVER_EMAIL的值为发件人
    会向ADMINS = (('1531391246', '1531391246@qq.com'),)中设置的邮箱发送邮件
"""
"""
    mail_managers(subject，message，fail_silently = False，connection = None，html_message = None)
    与上一个类似
"""


def send_mail_mass_async(*args, **kwargs):
    """
    Using celery to send email async
        message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
    message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])

    send_mass_mail((message1, message2), fail_silently=False)
    """

    send_mass_mail(*args, **kwargs)


############# 发送附件 #############
from django.core.mail import EmailMessage

"""
EmailMessage(
    subject='',
    body='',
    from_email=None,
    to=None,
    bcc=None,
    connection=None,
    attachments=None,
    headers=None,
    cc=None,
    reply_to=None,
)
subject：电子邮件的主题行。
body：正文。这应该是纯文本消息。
from_email：发件人的地址。这两个fred@example.com和 形式是合法的。如果省略，则使用该 设置。"Fred" <fred@example.com>DEFAULT_FROM_EMAIL
to：收件人地址列表或元组。
bcc：发送电子邮件时，“密件抄送”标题中使用的地址列表或元组。
connection：电子邮件后端实例。如果要对多个消息使用相同的连接，请使用此参数。如果省略，则在send()调用时创建一个新的连接。
attachments：要放入邮件的附件列表。这些可以是MIMEBase实例，也可以是三元组。(filename, content, mimetype)
headers：附加消息头的字典。键是标题名称，值是标题值。呼叫者应确保标题名称和值的格式正确无误。对应的属性是extra_headers。
cc：发送电子邮件时，“抄送”标题中使用的收件人地址列表或元组。
reply_to：发送电子邮件时，“回复至”标题中使用的收件人地址列表或元组。
email = EmailMessage(
    'Hello',
    'Body goes here',
    'from@example.com',
    ['to1@example.com', 'to2@example.com'],
    ['bcc@example.com'],
    reply_to=['another@example.com'],
    headers={'Message-ID': 'foo'},
)

"""


def send_mail_attach_async(*args, **kwargs):
    subject = "邮件附件发送测试"
    body = "测试邮件附件"
    from_email = settings.EMAIL_FROM
    to = ['1299793997@qq.com', '564060577@qq.com']

    message = EmailMessage(
        subject=subject,
        body=body,
        from_email=from_email,
        to=to,
        bcc=None,
        connection=None,
        attachments=None,
        headers=None,
        cc=None,
        reply_to=None,
    )
    message.content_subtype = "html"
    message.encoding = 'utf-8'
    message.attach_file('/home/code/scripts/scripts-py/_re.py')
    message.send()


############# 发送html邮件 #############
from django.core.mail import EmailMultiAlternatives

"""

EmailMultiAlternatives(
    subject='',
    body='',
    from_email=None,
    to=None,
    bcc=None,
    connection=None,
    attachments=None,
    headers=None,
    alternatives=None,
    cc=None,
    reply_to=None,
)
subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
text_content = 'This is an important message.'
html_content = '<p>This is an <strong>important</strong> message.</p>'
msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
msg.attach_alternative(html_content, "text/html")
msg.send()

msg = EmailMessage(subject, html_content, from_email, [to])
msg.content_subtype = "html"  # Main content is now text/html
msg.send()


"""


def send_mail_html_async(*args, **kwargs):
    subject = "邮件附件发送测试"
    body = 'This is an important message.'
    from_email = settings.EMAIL_FROM
    to = ['1299793997@qq.com', '564060577@qq.com']
    message = EmailMultiAlternatives(subject, body, from_email, to)

    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    html_content = '<p>http://39.105.100.168:8080/user/list/</p>'
    message.attach_alternative(html_content, "text/html")
    # 添加附件
    message.content_subtype = "html"
    message.encoding = 'utf-8'
    message.attach_file('/home/code/scripts/scripts-py/_re.py')
    message.send()
