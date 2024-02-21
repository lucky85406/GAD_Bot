import time

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from Module.messageModule import chk_mes
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
    a = 0
    if a == 0:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text='a quick reply message',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="message", text="one message")
                        )
                    ])))
        a +=1

    if Ukey() != "":
        line_bot_api.reply_message(event.reply_token, chk_mes(Ukey()))


'''
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
'''
# 執行
if __name__ == "__main__":
    app.run()
