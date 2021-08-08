#!/usr/bin/enve python
# -*- coding: utf-8 -*-
# author: Leo
# file: dingtalk
# datetime: 2021/8/3 2:01 下午
# Email: leo.minorui@gmail.com
# ide: PyCharm


from dingtalkchatbot.chatbot import DingtalkChatbot

from django.conf import settings

def send(message, at_mobiles=[]):
    # 引用settings里面配置的叮叮群消息通知的WebHook地址：
    webhook = settings.DINGTALK_WEB_HOOK

    # 初始化机器人小丁, 方式一：通常初始化方式
    xiaoding = DingtalkChatbot(webhook)

    # 方式二： 勾选"加签"选项时使用
    # xiaoding = DingtalkChatbot(webhook, secret=secret)

    # Text消息@所有人

    xiaoding.send_text(msg=('面试通知：%s' % message), at_mobiles= [] )