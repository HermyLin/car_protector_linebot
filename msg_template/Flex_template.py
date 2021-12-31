from linebot.models import FlexSendMessage
def dayornight():
    flex_message = FlexSendMessage(
                   alt_text='選擇時段',
                   contents= {
                                "type": "bubble",
                                "hero": {
                                "type": "image",
                                "url": "https://github.com/HermyLin/stealer/blob/main/bot_image/images.png",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "position": "relative"
                                        },
                                "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                            {
                                            "type": "text",
                                            "text": "請選擇時辰",
                                            "weight": "bold",
                                            "size": "xl"
                                            "contents": [],
                                            "color": "#876C5A"
                                            },    
                                            {
                                            "type": "text",
                                            "text": "貼心提醒：\n上午>00:00-11:59\n下午>12:00/23:59",
                                            "size": "xs",
                                            "margin": "sm"
                                            },
                                            {
                                            "type": "separator",
                                            "margin": "lg"
                                            },
                                            {
                                            "type": "box",
                                            "layout": "verical",
                                            "contents": [
                                                        {
                                                        "type": "button",
                                                        "action": {
                                                        "type": "message",
                                                        "label": "上午",
                                                        "text": "上午"
                                                        },
                                                        "style": "primary",
                                                        "height": "sm",
                                                        "color": "#797D62"
                                                        },
                                                        {
                                                        "type": "button",
                                                        "action": {
                                                        "type": "message",
                                                        "label": "下午",
                                                        "text": "下午"
                                                        },
                                                        "style": "primary",
                                                        "margin": "xxl",
                                                        "height": "sm",
                                                        "color": "#797D62"
                                                        }
                                                        ],
                                            "margin": "md"
                                            ]
                                            }
                                        }               
                                )                       
    return flex_message

def cartype_choose():
    flex_message = FlexSendMessage(
                   alt_text='選擇車型',
                   contents= {
                                "type": "bubble",
                                "hero": {
                                "type": "image",
                                "url": "https://images.twgreatdaily.com/images/elastic/iuP/iuPP1mwBJleJMoPMp5x0.jpg",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "cover",
                                "position": "relative"
                                        },
                                "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                            {
                                            "type": "text",
                                            "text": "請選擇車型",
                                            "weight": "bold",
                                            "size": "xl"
                                            "contents": [],
                                            "color": "#876C5A"
                                            },    
                                            #{
                                            #"type": "text",
                                            #"text": "",
                                            #"size": "xs",
                                            #"margin": "sm"
                                            #},
                                            {
                                            "type": "separator",
                                            "margin": "lg"
                                            },
                                            {
                                            "type": "box",
                                            "layout": "verical",
                                            "contents": [
                                                        {
                                                        "type": "button",
                                                        "action": {
                                                        "type": "message",
                                                        "label": "汽車\udbc0\udc49",
                                                        "text": "汽車"
                                                        },
                                                        "style": "primary",
                                                        "height": "sm",
                                                        "color": "#797D62"
                                                        },
                                                        {
                                                        "type": "button",
                                                        "action": {
                                                        "type": "message",
                                                        "label": "機車\udbc0\udc8c",
                                                        "text": "機車"
                                                        },
                                                        "style": "primary",
                                                        "height": "sm",
                                                        "color": "#797D62"
                                                        },
                                                        {
                                                        "type": "button",
                                                        "action": {
                                                        "type": "message",
                                                        "label": "腳踏車\udbc0\udc4b",
                                                        "text": "腳踏車"
                                                        },
                                                        "style": "primary",
                                                        "margin": "xxl",
                                                        "height": "sm",
                                                        "color": "#797D62"
                                                        }
                                                        ],
                                            "margin": "md"
                                            ]
                                            }
                                        }               
                                )                       
    return flex_message