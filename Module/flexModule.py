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
                "size": "mega",
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
                                            "size": "65px"
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
                                            "color": "#019858",
                                            "decoration": "underline"
                                        },
                                        {
                                            "type": "text",
                                            "text": "(2024.02.15前)",
                                            "size": "xl",
                                            "weight": "bold",
                                            "align": "center",
                                            "margin": "md"
                                        }
                                    ],
                                    "offsetEnd": "xl"
                                }
                            ]
                        }
                    ]
                },
                "hero": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "【去程】",
                                                    "weight": "bold",
                                                    "align": "end",
                                                    "size": "xl"
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
                                                    "text": "EGAS",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "→",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
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
                                                    "text": "T2",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "action": {
                                        "type": "message",
                                        "label": "EGAS to T2",
                                        "text": "EGAS to T2"
                                    },
                                    "margin": "xl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "【回程】",
                                                    "weight": "bold",
                                                    "align": "end",
                                                    "size": "xl"
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
                                                    "text": "T2",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "→",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
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
                                                    "text": "EGAS",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "margin": "25px",
                                    "action": {
                                        "type": "message",
                                        "label": "T2 to EGAS",
                                        "text": "T2 to EGAS"
                                    }
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "margin": "30px"
                        }
                    ],
                    "margin": "150px"
                },
                "styles": {
                    "header": {
                        "backgroundColor": "#98DED8",
                        "separator": True,
                        "separatorColor": "#000000"
                    }
                }
            },
            {
                "type": "bubble",
                "size": "mega",
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
                                            "size": "65px"
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
                                            "color": "#019858",
                                            "decoration": "underline"
                                        },
                                        {
                                            "type": "text",
                                            "text": "(2024.02.15後)",
                                            "size": "xl",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#FF0000",
                                            "margin": "md"
                                        }
                                    ],
                                    "offsetEnd": "xl"
                                }
                            ]
                        }
                    ]
                },
                "hero": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "【去程】",
                                                    "weight": "bold",
                                                    "align": "end",
                                                    "size": "xl"
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
                                                    "text": "EGAS",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "→",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
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
                                                    "text": "T2",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "action": {
                                        "type": "message",
                                        "label": "EGAS to T2(新)",
                                        "text": "EGAS to T2(新)"
                                    },
                                    "margin": "xl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "【回程】",
                                                    "weight": "bold",
                                                    "align": "end",
                                                    "size": "xl"
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
                                                    "text": "T2",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "→",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
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
                                                    "text": "EGAS",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl"
                                                }
                                            ],
                                            "width": "70px"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "margin": "25px",
                                    "action": {
                                        "type": "message",
                                        "label": "T2 to EGAS(新)",
                                        "text": "T2 to EGAS(新)"
                                    }
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [],
                            "margin": "30px"
                        }
                    ],
                    "margin": "150px"
                },
                "styles": {
                    "header": {
                        "separator": True,
                        "separatorColor": "#000000",
                        "backgroundColor": "#4EDED3"
                    }
                }
            }
        ]
    }
    return contents


def three_page(a, at, b, bt, c, ct):
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": a,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": at,
                        "text": at
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": b,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": bt,
                        "text": bt
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": c,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": ct,
                        "text": ct
                    }
                }
            }
        ]
    }
    return contents


def four_page(a, at, b, bt, c, ct, d, dt):
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": a,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": at,
                        "text": at
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": b,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": bt,
                        "text": bt
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": c,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": ct,
                        "text": ct
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": d,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "top",
                            "aspectRatio": "8.5:20"
                        }
                    ],
                    "paddingAll": "0px",
                    "action": {
                        "type": "message",
                        "label": dt,
                        "text": dt
                    }
                }
            }
        ]
    }
    return contents


def video_test_page(titleimg, title, titlecolor, flat, video):
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "size": "mega",
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
                                            "url": titleimg,
                                            "size": "70px"
                                        }
                                    ],
                                    "width": "70px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": title,
                                            "weight": "bold",
                                            "align": "center",
                                            "color": titlecolor,
                                            "decoration": "underline",
                                            "gravity": "center",
                                            "size": "27px"
                                        }
                                    ],
                                    "offsetEnd": "xl",
                                    "alignItems": "center",
                                    "justifyContent": "center",
                                    "width": "220px"
                                }
                            ],
                            "maxHeight": "80px"
                        }
                    ],
                    "maxHeight": "100px"
                },
                "hero": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
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
                                                    "url": "https://i.imgur.com/BmOoACT.png",
                                                    "size": "50px"
                                                }
                                            ],
                                            "maxWidth": "80px",
                                            "justifyContent": "center"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "行走路線平面圖",
                                                    "weight": "bold",
                                                    "align": "center",
                                                    "size": "xl",
                                                    "decoration": "underline",
                                                    "action": {
                                                        "type": "message",
                                                        "label": "action",
                                                        "text": flat
                                                    },
                                                    "gravity": "center",
                                                    "margin": "xl",
                                                    "offsetBottom": "md"
                                                }
                                            ],
                                            "maxWidth": "200px"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "action": {
                                        "type": "message",
                                        "label": "atob",
                                        "text": "atob"
                                    },
                                    "cornerRadius": "50px",
                                    "offsetTop": "10px",
                                    "margin": "15px"
                                },
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
                                                    "url": "https://i.imgur.com/cYKPlO2.png",
                                                    "size": "50px"
                                                }
                                            ],
                                            "justifyContent": "center",
                                            "maxWidth": "80px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "行走路線影片",
                                                    "align": "center",
                                                    "size": "xl",
                                                    "weight": "bold",
                                                    "decoration": "underline",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "action",
                                                        "uri": video,
                                                        "altUri": {
                                                            "desktop": video
                                                        }
                                                    },
                                                    "gravity": "center",
                                                    "margin": "xl",
                                                    "offsetBottom": "md",
                                                    "color": "#FF5151"
                                                }
                                            ],
                                            "maxWidth": "200px"
                                        }
                                    ],
                                    "alignItems": "center",
                                    "margin": "20px",
                                    "action": {
                                        "type": "message",
                                        "label": "atob",
                                        "text": "atob"
                                    },
                                    "cornerRadius": "50px",
                                    "offsetTop": "10px"
                                }
                            ],
                            "height": "160px"
                        }
                    ]
                },
                "styles": {
                    "hero": {
                        "backgroundColor": "#FFF3EE"
                    }
                }
            }
        ]
    }
    return contents


def transit_map():
    contents = {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
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
                                            "url": "https://i.imgur.com/yDuhMfq.png",
                                            "size": "70px"
                                        }
                                    ],
                                    "width": "70px",
                                    "height": "70px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "長興線",
                                            "weight": "bold",
                                            "align": "center",
                                            "color": "#FFD306",
                                            "decoration": "underline",
                                            "gravity": "center",
                                            "size": "27px"
                                        }
                                    ],
                                    "offsetEnd": "xl",
                                    "alignItems": "center",
                                    "justifyContent": "center",
                                    "width": "150px",
                                    "height": "80px"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "每日行駛",
                                    "size": "md",
                                    "weight": "bold",
                                    "color": "#FF0000",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "separator"
                        }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "長興01",
                                    "weight": "bold"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#0000E3",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#0000E3",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        }
                                    ],
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "5px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "15px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "16px"
                                        }
                                    ],
                                    "margin": "sm"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [],
                                    "borderWidth": "light",
                                    "borderColor": "#7B7B7B",
                                    "height": "1px",
                                    "width": "30px",
                                    "offsetTop": "8px",
                                    "margin": "md"
                                }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "長興02",
                                    "weight": "bold"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#0000E3",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#0000E3",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        }
                                    ],
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "5px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "15px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "16px"
                                        }
                                    ],
                                    "margin": "sm"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [],
                                    "borderWidth": "light",
                                    "borderColor": "#7B7B7B",
                                    "height": "1px",
                                    "width": "30px",
                                    "offsetTop": "8px",
                                    "margin": "md"
                                }
                            ],
                            "margin": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "長興03",
                                    "weight": "bold"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#0000E3",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#0000E3",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "30px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        }
                                    ],
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "5px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "15px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "16px"
                                        }
                                    ],
                                    "margin": "sm"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [],
                                    "borderWidth": "light",
                                    "borderColor": "#7B7B7B",
                                    "height": "1px",
                                    "width": "30px",
                                    "offsetTop": "8px",
                                    "margin": "md"
                                }
                            ],
                            "margin": "xxl"
                        }
                    ]
                }
            },
            {
                "type": "bubble",
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
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "From",
                                            "weight": "bold",
                                            "size": "xl",
                                            "align": "end",
                                            "color": "#7B7B7B"
                                        }
                                    ],
                                    "maxWidth": "80px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "廠辦園區",
                                            "weight": "bold",
                                            "size": "xxl",
                                            "align": "center"
                                        }
                                    ],
                                    "maxWidth": "150px"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "To",
                                            "size": "xl",
                                            "weight": "bold",
                                            "align": "end",
                                            "color": "#7B7B7B"
                                        }
                                    ],
                                    "maxWidth": "80px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "T2第二航廈",
                                            "align": "center",
                                            "size": "25px",
                                            "weight": "bold"
                                        }
                                    ],
                                    "maxWidth": "150px"
                                }
                            ],
                            "margin": "lg"
                        }
                    ],
                    "height": "120px",
                    "backgroundColor": "#B3D9D9"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "第一班",
                                    "weight": "bold"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "50px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#0000E3",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "50px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        }
                                    ],
                                    "offsetStart": "30px",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "19px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "13px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "8px"
                                        }
                                    ],
                                    "margin": "sm"
                                }
                            ],
                            "margin": "md"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "第二班",
                                    "weight": "bold"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "50px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#0000E3",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "50px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        }
                                    ],
                                    "offsetStart": "30px",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "19px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "13px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "8px"
                                        }
                                    ],
                                    "margin": "sm"
                                }
                            ],
                            "margin": "xl"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "第三班",
                                    "weight": "bold"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "50px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#0000E3",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "borderWidth": "light",
                                            "borderColor": "#7B7B7B",
                                            "height": "1px",
                                            "width": "50px",
                                            "offsetTop": "8px",
                                            "margin": "md"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [],
                                            "width": "15px",
                                            "height": "15px",
                                            "borderWidth": "medium",
                                            "borderColor": "#EA0000",
                                            "cornerRadius": "xxl",
                                            "margin": "md"
                                        }
                                    ],
                                    "offsetStart": "30px",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "19px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "13px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "07:20",
                                            "size": "sm",
                                            "offsetStart": "8px"
                                        }
                                    ],
                                    "margin": "sm"
                                }
                            ],
                            "margin": "xl"
                        }
                    ]
                }
            }
        ]
    }
    return contents
