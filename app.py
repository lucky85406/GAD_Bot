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
from Module.flexModule import transit, T2toEGAS
import json
import schedule


def my_schedule():
    print("Running!!")


job = schedule.Job(my_schedule, interval=60)
schedule.schedule(job)
while True:
    schedule.run_pending()
    time.sleep(60)

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

    if Ukey() == "交通車時刻表":
        line_bot_api.reply_message(event.reply_token,
                                   ImageSendMessage(original_content_url="https://i.imgur.com/Pw5ZxG1.jpg",
                                                    preview_image_url='https://i.imgur.com/Pw5ZxG1.jpg'))
    elif Ukey() == "長興線":
        line_bot_api.reply_message(event.reply_token,
                                   FlexSendMessage(alt_text='hi', contents=T2toEGAS()))
    elif Ukey() == "A15線":
        line_bot_api.reply_message(event.reply_token,
                                   FlexSendMessage(alt_text='hi', contents=transit("廠辦園區", "長興園區")))
    elif Ukey() == "T2 to EGAS":
        line_bot_api.reply_message(event.reply_token,
                                   ImageSendMessage(original_content_url="https://i.imgur.com/OAKjodG.jpg",
                                                    preview_image_url='https://i.imgur.com/OAKjodG.jpg'))
    elif Ukey() == "EGAS to T2":
        line_bot_api.reply_message(event.reply_token,
                                   ImageSendMessage(original_content_url="https://i.imgur.com/ZaP6Zpk.jpg",
                                                    preview_image_url='https://i.imgur.com/ZaP6Zpk.jpg'))
    else:
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text="服務開發中!"))


# 執行
if __name__ == "__main__":
    app.run()
