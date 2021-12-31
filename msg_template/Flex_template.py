from linebot.models import FlexSendMessage
def dayornight():
    flex_message = FlexSendMessage(
                    alt_text='選擇時段',
                    contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://transcode-v2.app.engoo.com/image/fetch/f_auto,c_limit,w_1280,h_800,dpr_2/https://assets.app.engoo.com/images/CGPkj72Wn3gPmu9ebqmpS1nGQNOZQlR70NilqMAWUBm.png",
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
            "size": "xs",
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
            "flex": 0
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
      }
    ],
    "position": "relative",
    "margin": "none"
  },
  "footer": {
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
      {
        "type": "spacer",
        "size": "xs"
      }
    ],
    "flex": 0,
    "borderWidth": "none",
    "cornerRadius": "none",
    "margin": "xs",
    "paddingAll": "lg"
  },
  "styles": {
    "footer": {
      "separator": True
    }
  }
}
    )                       
    return flex_message
