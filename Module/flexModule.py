import json
import requests

with open("config.txt", "r") as f:
    content = f.read()
    json_obj = json.loads(content)
    CHANNEL_ACCESS_TOKEN = json_obj["CHANNEL_ACCESS_TOKEN"]
    CHANNEL_SECRET = json_obj["CHANNEL_SECRET"]


def AtoB(title, a, b, c, d):
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "size": "giga",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://i.imgur.com/jpcsNZ9.png",
                                            "size": "5xl"
                                        }
                                    ],
                                    "width": "100px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "廠辦線",
                                            "size": "3xl",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#02DF82",
                                            "decoration": "underline"
                                        },
                                        {
                                            "type": "text",
                                            "text": "(2024.02.15前)",
                                            "size": "xl",
                                            "weight": "bold",
                                            "align": "center"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "lg"
                        }
                    ]
                },
                "hero": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "【去程】EGAS to T2",
                            "weight": "bold",
                            "align": "center",
                            "size": "xl",
                            "action": {
                                "type": "message",
                                "label": "【去程】EGAS to T2",
                                "text": "EGAS to T2"
                            }
                        },
                        {
                            "type": "text",
                            "text": "【回程】T2 to EGAS",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "margin": "xxl",
                            "action": {
                                "type": "message",
                                "label": "【回程】T2 to EGAS",
                                "text": "T2 to EGAS"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "margin": "lg"
                        }
                    ]
                }
            },
            {
                "type": "bubble",
                "size": "giga",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://i.imgur.com/jpcsNZ9.png",
                                            "size": "5xl"
                                        }
                                    ],
                                    "width": "50px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "廠辦線",
                                            "size": "3xl",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#02DF82",
                                            "decoration": "underline"
                                        },
                                        {
                                            "type": "text",
                                            "text": "(2024.02.15後)",
                                            "size": "xl",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#FF0000"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "type": "separator",
                            "margin": "lg"
                        }
                    ]
                },
                "hero": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "【去程】EGAS to T2",
                            "weight": "bold",
                            "align": "center",
                            "size": "xl",
                            "action": {
                                "type": "message",
                                "label": "【去程】EGAS to T2",
                                "text": "EGAS to T2"
                            }
                        },
                        {
                            "type": "text",
                            "text": "【回程】T2 to EGAS",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center",
                            "margin": "xxl",
                            "action": {
                                "type": "message",
                                "label": "【回程】T2 to EGAS",
                                "text": "T2 to EGAS"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "margin": "lg"
                        }
                    ]
                }
            }
        ]
    }
    return contents
