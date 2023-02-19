import os
import time
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP
import requests


def txt_get(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read().split('\n')
        return data


def txt_set(data, file_path):
    """请输入列表，会自动转换格式"""
    with open(file_path, 'r+') as f:
        for d in data:
            f.write(f'{d}\n')


def send_email_qq(user_id, title, content):
    # 请自行修改下面的邮件发送者和接收者
    sender = '672545360@qq.com'
    receivers = [f'{user_id}@qq.com']
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header('洛瑜', 'utf-8')
    message['To'] = Header(user_id, 'utf-8')
    message['Subject'] = Header(title, 'utf-8')
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'lwygaghmtitibcgf')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


def send_email_163(user_id, title, content):
    # 请自行修改下面的邮件发送者和接收者
    sender = '@163.com'
    receivers = [f'{user_id}@qq.com']
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header('biliup bot', 'utf-8')
    message['To'] = Header(user_id, 'utf-8')
    message['Subject'] = Header(title, 'utf-8')
    smtper = SMTP('smtp.163.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, '')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


def send_msg(group_id, message):
    params = {
        "message_type": 'group',
        "group_id": group_id,
        "message": message
    }
    url = "http://127.0.0.1:8000/send_msg"
    return requests.get(url, params=params).json()
