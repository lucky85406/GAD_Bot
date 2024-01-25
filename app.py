import time

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage
)
from Module.flexModule import transit, AtoB, gigaPage
import json
import threading
import requests

app = Flask(__name__)

with open("config.txt", "r") as f:
    content = f.read()
    json_obj = json.loads(content)
    CHANNEL_ACCESS_TOKEN = json_obj["CHANNEL_ACCESS_TOKEN"]
    CHANNEL_SECRET = json_obj["CHANNEL_SECRET"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route("/")
def home():
    return 'home OK'


# 監聽所有來自 /callback 的 Post Request


@app.route("/callback", methods=['POST'])
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def function(event):
    # 取得使用者輸入訊息
    def Ukey():
        return event.message.text

    if Ukey() == "廠辦線":
        line_bot_api.reply_message(event.reply_token,
                                   FlexSendMessage(alt_text='hi',
                                                   contents=AtoB("廠辦線", "【去程】EGAS to T2", "EGAS to T2",
                                                                 "【回程】T2 to EGAS", "T2 to EGAS")))
    elif Ukey() == "EGAS to T2":
        line_bot_api.reply_message(event.reply_token,
                                   ImageSendMessage(original_content_url="https://i.imgur.com/tqTCfWQ.jpg",
                                                    preview_image_url='https://i.imgur.com/tqTCfWQ.jpg'))
    elif Ukey() == "T2 to EGAS":
        line_bot_api.reply_message(event.reply_token,
                                   ImageSendMessage(original_content_url="https://i.imgur.com/NPhQEHk.jpg",
                                                    preview_image_url='https://i.imgur.com/NPhQEHk.jpg'))
    elif Ukey() == "長興線":
        line_bot_api.reply_message(event.reply_token,
                                   ImageSendMessage(original_content_url="https://i.imgur.com/tHiDkuI.jpg",
                                                    preview_image_url='https://i.imgur.com/tHiDkuI.jpg'))
    elif Ukey() == "A15線":
        line_bot_api.reply_message(event.reply_token,
                                   ImageSendMessage(original_content_url="https://i.imgur.com/3CM7rat.jpg",
                                                    preview_image_url='https://i.imgur.com/3CM7rat.jpg'))
    elif Ukey() == "T2walk":
        line_bot_api.reply_message(event.reply_token,
                                   ImageSendMessage(original_content_url="https://i.imgur.com/58RNnJz.jpg",
                                                    preview_image_url='https://i.imgur.com/58RNnJz.jpg'))
    elif Ukey() == "EGASwalk":
        line_bot_api.reply_message(event.reply_token,
                                   ImageSendMessage(original_content_url="https://i.imgur.com/8EFEpV3.jpg",
                                                    preview_image_url='https://i.imgur.com/8EFEpV3.jpg'))
    elif Ukey() == "information":
        line_bot_api.reply_message(event.reply_token,
                                   FlexSendMessage(alt_text='hi',
                                                   contents=gigaPage()))
    else:
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text="服務開發中!"))


def wake_up_render():
    while True:
        url = "https://gadtransit.onrender.com"
        res = requests.get(url)
        if res.status_code == 200:
            print("awaking!!")
        else:
            print("awaking error!!")
        time.sleep(870)


threading.Thread(target=wake_up_render).start()

# 執行
if __name__ == "__main__":
    app.run()
