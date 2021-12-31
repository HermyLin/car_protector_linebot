from linebot.models import FlexSendMessage
def result(map_for_user,sentence,risk):
    sentence = sentence.split("/")
    flex_message = FlexSendMessage(
    contents = {
        "type": "bubble",
        "hero": {
        "type": "image",
        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/ (絕對路徑)"+risk+".png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
        "type": "uri",
        "uri": "http://linecorp.com/"
        }}
        ,
        "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "判斷結果:" + risk,
            "weight": "bold",
            "size": "xl"
        },
        {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": sentence(0)+"\n" + sentence(1) + "\n" + sentence(2),
                "wrap": true,
                "color": "#666666",
                "size": "md",
                "flex": 5
              }
                        ]
          }
                       ]
      }
                       ]
                },
                
        "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
        {
            "type": "button",
            "style": "link",
            "height": "sm",
            "action": {
            "type": "uri",
            "label": "查看過去竊案地圖",
            "uri": map_for_user
                      }
        },
        {
        "type": "spacer",
        "size": "sm"
        }
                    ],
        "flex": 0
                 }
              }