from linebot.models import FlexSendMessage
def dayornight():
    flex_message = FlexSendMessage(
                    alt_text='白天還是晚上呢？',
                    contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://github.com/HermyLin/car_protector_linebot/blob/main/bot_image/01_day_or_night.jpg?raw=true",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "margin": "none",
    "position": "relative",
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "請選擇時段",
        "weight": "bold",
        "size": "xl",
        "color": "#00bfff",
        "margin": "none"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "xs",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
            "margin": "none",
            "position": "relative"
          },
          {
            "type": "text",
            "size": "sm",
            "color": "#999999",
            "margin": "xs",
            "text": "貼心提醒："
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "xs",
        "contents": [
          {
            "type": "text",
            "text": "上午為 00:00－11:59",
            "size": "xs",
            "color": "#999999",
            "margin": "none",
          }
        ],
        "spacing": "none"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "xs",
        "contents": [
          {
            "type": "text",
            "text": "下午為 12:00－23:59",
            "size": "xs",
            "color": "#999999",
            "margin": "none"
          }
        ],
        "spacing": "none"
      },
      {
        "type": "separator",
        "margin": "lg"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "spacing": "md",
        "contents": [
           {
            "type": "button",
            "style": "primary",
            "height": "sm",
            "action": {
                "type": "message",
                "label": "上午",
                "text": "上午"
            },
        "margin": "none",
        "color": "#deb887"
        },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "下午",
          "text": "下午"
        },
        "color": "#deb887"
      },
    ],
    "margin": "xs",
    "paddingAll": "lg"
        }
        ]
    }
}

    )                       
    return flex_message

def cartype_choose():
    flex_message = FlexSendMessage(
                    alt_text="選車中",
                    contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://github.com/HermyLin/car_protector_linebot/blob/main/bot_image/03_cartype.jpg?raw=true",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "margin": "none",
    "position": "relative",
    "gravity": "top"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "請選擇車種",
        "weight": "bold",
        "size": "xl",
        "color": "#00bfff",
        "margin": "none"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "xs",
        "contents": [
          {
            "type": "text",
            "size": "sm",
            "color": "#999999",
            "margin": "none",
            "text": "要停放什麼車呢？"
          }
        ]
      },
      {
        "type": "separator",
        "margin": "lg"
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "md",
        "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "message",
          "label": "汽車",
          "text": "汽車"
        },
        "margin": "none",
        "color": "#deb887",
        "height": "sm",
        "position": "relative"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "機車",
          "text": "機車"
        },
        "color": "#deb887"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "腳踏車",
          "text": "腳踏車"
        },
        "color": "#deb887"
      }
    ],
    "borderWidth": "none",
    "cornerRadius": "none",
    "margin": "xs",
    "paddingAll": "lg",
    "paddingTop": "md",
    "paddingBottom": "lg",
    "paddingStart": "xxl",
    "paddingEnd": "xxl"
  }
   ]
  }
}
    )
    return flex_message
