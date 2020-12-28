# -*-coding:utf-8 -*-
# File : RunTestCase.py
# @Time : 2020/12/25 18:45
# @Author : Sf
# version : python 3.7.8


class LoginData(object):
    """用户登录测试数据"""

    login_success_data = [
        (
            "bruce2025",
            "bruce@2025",
            "bruce2025@126.com"
        )
    ]

    login_fail_data = [
        (
            "linuxxiaochao",
            "",
            "请输入密码"
        ),
        (
            "",
            "xiaochao11520",
            "请输入帐号"
        ),
        (
            "linux",
            "xiaochao",
            "请先进行验证"
        )
    ]


if __name__ == '__main__':
    pass
