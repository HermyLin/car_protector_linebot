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

#frontend
import os
import time
import json
import re
import requests

#backend
from math import sqrt
from math import cos
from math import sin
import math
import pandas as pd
import csv

#載入其他py檔
from msg_template import Flex_template, Result_flex

#------------------------------------------
# 定義function與基礎設置
#---------------car type-------------------
car_type_list = ["汽車","機車","腳踏車"]
#----------------時間設定-------------------
time_label = ['上午','下午']
times = ['00:00-01:59','02:00-03:59','04:00-05:59','06:00-07:59','08:00-09:59','10:00-11:59','12:00-13:59','14:00-15:59','16:00-17:59','18:00-19:59','20:00-21:59','22:00-23:59']
#------------------------------------------
def rad(d):
    r = d * math.pi / 180.0
    return r

def getDistance(lat1, lng1, lat2, lng2):
    EARTH_REDIUS = 6378.137
    lat1 = float(lat1)
    lng1 = float(lng1)
    lat2 = float(lat2)
    lng2 = float(lng2)
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(sin(a/2), 2) + cos(radLat1) * cos(radLat2) * math.pow(sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return s

def map_for_user(case,time):
    time = int(time.split(":")[0])
    if time % 2 != 0:
        time_map = ((time-1)/2)-1
    else:
        time_map = (time/2)-1
    df = pd.read_csv("stolen_map.csv")
    bike_map_dict = {}
    motor_map_dict = {}
    car_map_dict = {}   
    bike_map = ['bike0','bike2','bike4','bike6','bike8','bike10','bike12','bike14','bike16','bike18','bike20','bike22']
    motor_map = ['motor0','motor2','motor4','motor6','motor8','motor10','motor12','motor14','motor16','motor18','motor20','motor22']          
    car_map = ['car0','car2','car4','car6','car8','car10','car12','car14','car16','car18','car20','car22']
    
    if case == "汽車":
        for time_map in range(len(car_map)):
            car_map_website = car_map[time_map]
            car_map_dict[car_map_website] = df[car_map_website]
            map_for_user_URL = car_map_dict[map[time_map]]

    elif case == "機車":
        for time_map in range(len(motor_map)):
            motor_map_website = motor_map[time_map]
            motor_map_dict[motor_map_website] = df[motor_map_website]
            map_for_user_URL = motor_map_dict[map[time_map]]

    elif case == "腳踏車":
        for time_map in range(len(bike_map)):
            bike_map_website = bike_map[time_map]
            bike_map_dict[bike_map_website] = df[bike_map_website]
            map_for_user_URL = bike_map_dict[map[time_map]]

    return(map_for_user_URL)

def case_count(time, local_x, local_y):
    time = int(time.split(":")[0])
    if time % 2 != 0:
        time -= 1
        num_sum = []
        range_km = 2
    
        for case in ["car","moto","bike"]:
            num = 0

            #df_case = pd.read_csv(f"2hr_location/{case}_{time}.csv",encoding='big5')
            file = open(f"{case}_{time}.csv", "r",encoding='big5')
            for line in file:
                line = line.strip(" ")
                line = line.strip("\n")
                line = line.split(",")
                case_x = line[4]
                case_y = line[5]
                
                if getDistance(case_x, case_y, local_x, local_y) <= range_km:
                    num +=1       
            num_sum.append(num)
    return num_sum 
  
def risk_judge(num_sum):        
    num_tot = sum(num_sum)
    range_km = 2

    risk = "略微安全"
    if num_tot >= 5:
        risk = "危險"
    elif num_tot <= 1:
        risk = "安全"
        
    message_result = str(num_sum[0])+ "件汽車竊盜/" + str(num_sum[1]) + "件機車竊盜/" + str(num_sum[2]) + "件腳踏車竊盜"
    return (risk, message_result)

def results_for_all(car_type,user_time,u_lat,u_lon):
    numbers_for_all_case = case_count(user_time,u_lat,u_lon) 
    risk, sentence = risk_judge(numbers_for_all_case)
    map_for_user_URL = map_for_user(car_type,user_time)
    return (risk, sentence, map_for_user_URL)

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
        car_type = event.message.text
        
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
    #user_address = event.message.address

    risk, sentence, map_for_user_URL = results_for_all(car_type,user_time,u_lat,u_lon)
    
    if risk == "危險":
        flex_message_result = FlexSendMessage(
                                        alt_text='結果出爐囉～',
                                        contents= Result_template.result_dangerous(car_type,map_for_user_URL,sentence),
                                        quick_reply= QuickReply(items=[QuickReplyButton(action=LocationAction(label="再定位一次!"))]))

    elif risk == "略為安全"
        flex_message_result = FlexSendMessage(
                                        alt_text='結果出爐囉～',
                                        contents= Result_template.result_little_dangerous(car_type,map_for_user_URL,sentence),
                                        quick_reply= QuickReply(items=[QuickReplyButton(action=LocationAction(label="再定位一次!"))]))

    elif risk == "安全"
        flex_message_result = FlexSendMessage(
                                        alt_text='結果出爐囉～',
                                        contents= Result_template.result_safe(car_type,map_for_user_URL,sentence),
                                        quick_reply= QuickReply(items=[QuickReplyButton(action=LocationAction(label="再定位一次!"))]))
                                        
    line_bot_api.reply_message(event.reply_token,flex_message_result) 

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
