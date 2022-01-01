from linebot.models import FlexSendMessage
def result_dangerous(car_type,map_for_user_URL,sentence):
    sentence_cut = sentence.split("/")
    watch_map = "看看"+car_type+"過去竊案地圖"
    flex_message = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://images.twgreatdaily.com/images/elastic/iuP/iuPP1mwBJleJMoPMp5x0.jpg",
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
        "text": "判斷結果：危險！",
        "weight": "bold",
        "size": "xl",
        "color": "#ff0000",
        "margin": "none"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "sm",
        "contents": [
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": "根據分析結果，您附近2公里有："
          },
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": sentence_cut[0]
          },
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": sentence_cut[1]
          },
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": sentence_cut[2]
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
        "layout": "vertical",
        "spacing": "md",
        "contents": [
        {
            "type": "button",
            "action": {
            "type": "uri",
            "label": watch_map,
            "uri": map_for_user_URL
			},
        "margin": "none",
        "color": "#cd853f",
        "height": "sm",
        "position": "relative",
        "style": "link"
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
      ],
    "position": "relative",
    "margin": "none"
  }
}
    return flex_message
    
def result_little_dangerous(car_type,map_for_user_URL,sentence):
    sentence_cut = sentence.split("/")
    watch_map = "看看"+car_type+"過去竊案地圖"
    flex_message = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://images.twgreatdaily.com/images/elastic/iuP/iuPP1mwBJleJMoPMp5x0.jpg",
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
        "text": "判斷結果：危險！",
        "weight": "bold",
        "size": "xl",
        "color": "#ff0000",
        "margin": "none"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "sm",
        "contents": [
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": "根據分析結果，您附近2公里有："
          },
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": sentence_cut[0]
          },
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": sentence_cut[1]
          },
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": sentence_cut[2]
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
        "layout": "vertical",
        "spacing": "md",
        "contents": [
        {
            "type": "button",
            "action": {
            "type": "uri",
            "label": watch_map,
            "uri": map_for_user_URL
			},
        "margin": "none",
        "color": "#cd853f",
        "height": "sm",
        "position": "relative",
        "style": "link"
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
      ],
    "position": "relative",
    "margin": "none"
  }
}
    return flex_message

def result_safe(car_type,map_for_user_URL,sentence):
    sentence_cut = sentence.split("/")
    watch_map = "看看"+car_type+"過去竊案地圖"
    flex_message = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://images.twgreatdaily.com/images/elastic/iuP/iuPP1mwBJleJMoPMp5x0.jpg",
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
        "text": "判斷結果：危險！",
        "weight": "bold",
        "size": "xl",
        "color": "#ff0000",
        "margin": "none"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "sm",
        "contents": [
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": "根據分析結果，您附近2公里有："
          },
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": sentence_cut[0]
          },
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": sentence_cut[1]
          },
          {
            "type": "text",
            "size": "sm",
            "color": "#000000",
            "margin": "none",
            "text": sentence_cut[2]
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
        "layout": "vertical",
        "spacing": "md",
        "contents": [
        {
            "type": "button",
            "action": {
            "type": "uri",
            "label": watch_map,
            "uri": map_for_user_URL
			},
        "margin": "none",
        "color": "#cd853f",
        "height": "sm",
        "position": "relative",
        "style": "link"
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
      ],
    "position": "relative",
    "margin": "none"
  }
}
    return flex_message

