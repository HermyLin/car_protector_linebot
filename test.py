# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021
@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com
Line Bot聊天機器人
第一章 Line Bot申請與串接
Line Bot機器人串接與測試
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
#line_bot_api = LineBotApi('你自己的token')
line_bot_api = LineBotApi('6miWE3Y5LfGTx4CIcVCGoapWfimm+8T0t6CoD5ZHqp0WUE59+/C3TgnJWqlqO6/m/H1yO8TUY+uabMjAmDTdWtc1EED8Y/1xkI/rp4BF3WOK6G32Oc6Gh1kHveeSCR0lntMHLnywb6m3bvMRLElZYAdB04t89/1O/w1cDnyilFU=')

# 必須放上自己的Channel Secret
#handler = WebhookHandler('你自己的secret')
handler = WebhookHandler('d8854482344a37ad58e7b512629cc206')

#line_bot_api.push_message('你自己的ID', TextSendMessage(text='你可以開始了'))
line_bot_api.push_message('Ub91b0ca857ac49515bcfce296d54baf6', TextSendMessage(text='讓我們開始吧！'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])    #route路由器
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

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
    if event.message.text in == "機車":
        car_type = event.message.text    
        text_message_location = TextSendMessage(text='請分享位置給我，讓我守護您愛車的安全\udbc0\udc2e', 
                                quick_reply=QuickReply(items=[
                                QuickReplyButton(action=LocationAction(label="點點我分享"))]))    
        line_bot_api.reply_message(event.reply_token,text_message_location)
    elif event.message.text == "問題回報":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "先這樣"))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "先這樣"))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text= Text_template.user_report()))
        #製作問題回報表單(google)
    else:
        line_bot_api.reply_message(event.reply_token,"Oops!小守找不到您的資訊呢～")
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text="Oops!小守找不到您的資訊呢～"))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text = Text_template.keyword_warning_text()))
'''
def handle_message(event):
    if event.message.text == "定位":
        text_message_location = TextSendMessage(text='偷偷分享位置給我，我才能守護你的安全喔！\udbc0\udc2e',
                                                quick_reply=QuickReply(items=[
                                                QuickReplyButton(action=LocationAction(label="點點我分享"))]))
        line_bot_api.reply_message(event.reply_token,text_message_location)

    else:
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token,message)
'''
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
