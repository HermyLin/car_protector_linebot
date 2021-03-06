# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import os
import time
import json
import csv
import re
import requests
import pandas as pd

#載入我們的py檔
from msg_template import Flex_template, Result_flex

#------------------------------------------
# 定義function與基礎設置
#---------------car type-------------------
car_type_list = ["汽車","機車","腳踏車"]
#----------------時間設定-------------------
time_label = ['上午','下午']
times = ['00:00-01:59','02:00-03:59','04:00-05:59','06:00-07:59','08:00-09:59','10:00-11:59','12:00-13:59','14:00-15:59','16:00-17:59','18:00-19:59','20:00-21:59','22:00-23:59']
#------------------------------------------


#----------------------------------------------
#LINE聊天機器人的基本資料
app = Flask(__name__)

#line_bot_api = LineBotApi('你自己的token')
line_bot_api = LineBotApi('g5sIQeW/GQj6y3+giEq5X85VaQzPodMv6D0o4PWKJQxezU+3IX++uqqMLOsgWDJ7EIdTeCInkRBAgMQXAfqPhWLvo+/k2yqKewC63eZORQxJsgiUt9FmIQmwDmGmgnBGaS/usc7T6EV4/uFv6E1eDQdB04t89/1O/w1cDnyilFU=')

#handler = WebhookHandler('你自己的secret')
handler = WebhookHandler('ae8a10ffbeda85e0e00dcbb41f4f9f47')

#line_bot_api.push_message('你自己的ID', TextSendMessage(text='你可以開始了'))
line_bot_api.push_message('Ub91b0ca857ac49515bcfce296d54baf6', TextSendMessage(text='讓我們開始吧！'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/", methods=['GET'])
def hello():
    return "Hello Stealer!"

@app.route("/callback", methods=['POST'])    #route路由器
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print("Request body: " + body, "Signature: " + signature)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):
    #選擇時間
    if event.message.text == "選擇時段":
        #送去Flex_template.py
        flex_message_time = Flex_template.dayornight()
        line_bot_api.reply_message(event.reply_token,flex_message_time)
    
    elif event.message.text == "上午" or event.message.text == "下午":
        #讀json檔 for choose time
        period_file = open('json_robot/json_period.json', encoding="utf8") 
        period_choose = json.load(period_file) 
    
        for i,tt in enumerate(time_label):
            if event.message.text == tt:
                flex_message_period = FlexSendMessage(alt_text= tt + "時段", contents= period_choose[i])
                line_bot_api.reply_message(event.reply_token,flex_message_period) 
        period_file.close()
        
#選時間 > 選車型
    elif event.message.text in times:
        temp_time = event.message.text
        user_time = temp_time.split("-")[0]
        #送去Flex_template.py
        flex_message_car = Flex_template.cartype_choose()
        line_bot_api.reply_message(event.reply_token,flex_message_car)  
    
    #抓時間 > 選車型
    elif event.message.text == "自動查找": 
        user_time = time.strftime('%H:%M', time.localtime())
        #送去Flex_template.py
        flex_message_car = Flex_template.cartype_choose()
        line_bot_api.reply_message(event.reply_token,flex_message_car)
        
    elif event.message.text == car_type_list[0] or event.message.text == car_type_list[1] or event.message.text == car_type_list[2]:
        text_message_location = TextSendMessage(text='偷偷分享位置給我，我才能守護你的安全喔！\udbc0\udc2e',
                                                quick_reply=QuickReply(items=[
                                                QuickReplyButton(action=LocationAction(label="點點我分享"))]))
        line_bot_api.reply_message(event.reply_token,text_message_location)

    elif event.message.text == "問題回報":
        message = TextSendMessage(text="no problem!")
        line_bot_api.reply_message(event.reply_token,message)
        
    else:
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token,message)

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    u_lat = event.message.latitude  #緯度
    u_lon = event.message.longitude #經度
    user_address = event.message.address
    reply_location = str(u_lat) + ", " + str(u_lon)
    line_bot_api.reply_message(event.reply_token,reply_location)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
