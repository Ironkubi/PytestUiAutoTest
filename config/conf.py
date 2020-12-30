# -*-coding:utf-8 -*-
# File : conf.py
# @Time : 2020/12/25 18:47
# @Author : Sf
# version : python 3.7.8
from datetime import datetime
import os

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(ROOT_DIR)
# 报告目录
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
print(REPORT_DIR)
# ui对象库config.ini文件所在目录
CONF_PATH = os.path.join(ROOT_DIR, 'config', 'config.ini')
print(CONF_PATH)
# 测试数据所在目录
DATA_Path = os.path.join(ROOT_DIR, 'data', 'tcData.xlsx')
print(DATA_Path)
# 当前时间
CURRENT_TIME = datetime.now().strftime('%H_%M_%S')

# 邮件配置信息
# 邮件服务器
SMTP_SERVER = 'smtp.qq.com'
# 发送者
FROM_USER = '账号@qq.com'
# 发送者密码
FROM_PASSWORD = 'mhxvqpewblldbjhf'
# 接收者
TO_USER = ['账号@qq.com']  # 可以同时发送给多人，追加到列表中
# 邮件标题
SUBJECT = 'xx项目自动化测试报告'
# 邮件正文
CONTENTS = '测试报告正文'
# 报告名称
HTML_NAME = 'testReport{}.html'.format(CURRENT_TIME)
print(HTML_NAME)
