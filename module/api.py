import os
import time
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP
import requests

# go-cqhttp 发信端口
listen_port = 8000


def send_msg(uid, message, message_type=0):
    """
    默认发送私聊信息
    如修改message_type为1，则发生群聊信息
    """
    if message_type == 0:
        # 发送私聊信息
        params = {
            "message_type": 'private',
            "user_id": str(uid),
            "message": message
        }
        url = f"http://127.0.0.1:{listen_port}/send_msg"
        return requests.get(url, params=params).json()
    else:
        # 发送群聊信息
        params = {
            "message_type": 'group',
            "group_id": str(uid),
            "message": message
        }
        url = f"http://127.0.0.1:{listen_port}/send_msg"
        return requests.get(url, params=params).json()

