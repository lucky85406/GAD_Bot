import json
import requests

with open("config.txt", "r") as f:
    content = f.read()
    json_obj = json.loads(content)
    CHANNEL_ACCESS_TOKEN = json_obj["CHANNEL_ACCESS_TOKEN"]
    CHANNEL_SECRET = json_obj["CHANNEL_SECRET"]


def AtoB(title, a, b, c, d):
    contents = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": title,
                    "weight": "bold",
                    "size": "xl",
                    "align": "center"
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
                        "type": "message",
                        "label": a,
                        "text": b
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "message",
                        "label": c,
                        "text": d
                    }
                }
            ],
            "flex": 0
        }
    }
    return contents


def rmenu_design():
    headers = {'Authorization': f'Bearer {CHANNEL_ACCESS_TOKEN}', 'Content-Type': 'application/json'}
    body = {'size': {'width': 2500, 'height': 1600},
            'selected': 'true',
            'name': 'Richmenu demo',
            'chatBarText': 'Richmenu demo',
            'areas': [
                {'bounds': {'x': 341, 'y': 75, 'width': 560, 'height': 340},
                 'action': {'type': 'message', 'text': '電器'}},
                {'bounds': {'x': 1434, 'y': 229, 'width': 930, 'height': 340},
                 'action': {'type': 'message', 'text': '運動用品'}},
                {'bounds': {'x': 122, 'y': 641, 'width': 560, 'height': 340},
                 'action': {'type': 'message', 'text': '客服'}},
                {'bounds': {'x': 1012, 'y': 645, 'width': 560, 'height': 340},
                 'action': {'type': 'message', 'text': '餐廳'}},
                {'bounds': {'x': 1813, 'y': 677, 'width': 560, 'height': 340},
                 'action': {'type': 'message', 'text': '鞋子'}},
                {'bounds': {'x': 423, 'y': 1203, 'width': 560, 'height': 340},
                 'action': {'type': 'message', 'text': '美食'}},
                {'bounds': {'x': 1581, 'y': 1133, 'width': 560, 'height': 340},
                 'action': {'type': 'message', 'text': '衣服'}}
            ]}
    req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', headers=headers,
                           data=json.dumps(body).encode('utf-8'))
    print(req.text)
