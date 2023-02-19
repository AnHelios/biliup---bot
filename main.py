import os
import time
import requests
from module import api, function


def upload_notice(ds_update_log_path, uid, message_type):
    if not os.path.exists(ds_update_log_path):
        print(f'未检测到ds_update.log文件存在，请您确定路径正确与否！')
        return
    while True:
        data = function.txt_get(ds_update_log_path)
        # 检查在ds_update.log文件中是否有稿件上传成功提示
        if '上传成功' in ''.join(data):
            # 检查在ds_update.log文件中：稿件上传成功提示的所在行数
            for line in data:
                if '上传成功' in line:
                    # 以下双重if如果同时成立，则表示稿件上传成功的时间 与 当前时间的小时数和分钟数一致
                    day = line[0:10]
                    hour = line[11:16]
                    if day == time.strftime("%Y-%m-%d"):
                        if hour == time.strftime("%H:%M"):
                            bvid = line.split("'bvid': '")[1].split("'}}")[0]
                            print(f"您的稿件{bvid}已于{time.strftime('%Y-%m-%d %H:%M:%S')}上传成功！")
                            api.send_msg(uid, f"您的稿件{bvid}已于{time.strftime('%Y-%m-%d %H:%M:%S')}上传成功！", message_type)
                            print("脚本等待下一次执行！")
                            time.sleep(60)
        time.sleep(10)
        # print(time.strftime('%Y-%m-%d %H:%M:%S'))


if __name__  == '__main__':
    print('biliup-bot开始执行')
    # ds_update.log文件的所在目录，请跟随以下实例填写
    ds_update_log_path = r'D:\biliup\ds_update.log'  # 请填写文件完整地址：如：D:\biliup\ds_update.log
    # 消息发送类型，0为发送私聊信息，1为群聊信息
    message_type = 0
    # 消息接收的私人QQ或者群号
    uid = '114514'
    # 启动go-cqttp，如未登录，请在弹出的窗口处进行扫码登陆
    os.startfile(os.path.join(os.getcwd(), 'go-cqhttp.bat'))
    # 开启稿件上传监听
    upload_notice(ds_update_log_path, uid, message_type)
