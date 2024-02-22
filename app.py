import datetime
import json
import sqlite3
import pandas as pd
import pytz
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import *
from Module.messageModule import chk_mes

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

    # 取得使用者ID
    def Uid():
        return event.source.user_id
    def select_data():
        conn = sqlite3.connect('Data/TestDB.db')
        res = pd.read_sql("SELECT * FROM MY_TABLE", conn)
        conn.close()
        return res["NAME"][0]
    def insert_data(n):
        conn = sqlite3.connect('Data/TestDB.db')
        c = conn.cursor()
        c.execute(f'INSERT INTO MY_TABLE (NAME) VALUE ("{n}")')
        conn.commit()
        conn.close()
        return True
    now = datetime.datetime.now(pytz.timezone("Asia/Taipei"))
    nd = f"{now.year}/{now.month}/{now.day} {now.hour}:{now.minute}"

    if "IN/" in Ukey():
        sp_name = Ukey().split('/')[1]
        if insert_data(sp_name):
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="success"))
    elif Ukey() != "":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=select_data()))


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
