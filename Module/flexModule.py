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


def transit_map(body_contents):
    contents = {
        "type": "carousel",
        "contents": body_contents
    }
    return contents


def step_choice(title, titlecolor, st, se):
    contents = {
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
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": title,
                                    "size": "xxl",
                                    "weight": "bold",
                                    "align": "center",
                                    "gravity": "center",
                                    "offsetTop": "10px"
                                }
                            ],
                            "width": "100px",
                            "borderWidth": "medium",
                            "borderColor": titlecolor,
                            "cornerRadius": "lg",
                            "height": "65px",
                            "backgroundColor": "#D2E9FF"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "地點選擇",
                                    "size": "xxl",
                                    "weight": "bold",
                                    "offsetTop": "13px",
                                    "offsetStart": "5px"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": st,
                            "size": "xl",
                            "weight": "bold",
                            "margin": "lg"
                        }
                    ]
                },
                {
                    "type": "separator",
                    "margin": "sm"
                }
            ],
            "background": {
                "type": "linearGradient",
                "angle": "0deg",
                "startColor": "#FFFFFF",
                "endColor": "#D1E9E9"
            }
        },
        "body": {
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
                                    "text": "大園",
                                    "size": "30px",
                                    "weight": "bold"
                                }
                            ],
                            "justifyContent": "center",
                            "alignItems": "center",
                            "borderWidth": "normal",
                            "borderColor": "#000000",
                            "height": "80px",
                            "cornerRadius": "xxl",
                            "width": "110px",
                            "backgroundColor": "#FFEEDD",
                            "action": {
                                "type": "message",
                                "label": "大園",
                                "text": se + "大園"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "長興",
                                    "size": "30px",
                                    "weight": "bold"
                                }
                            ],
                            "justifyContent": "center",
                            "alignItems": "center",
                            "height": "80px",
                            "borderWidth": "normal",
                            "borderColor": "#000000",
                            "cornerRadius": "xxl",
                            "width": "110px",
                            "margin": "md",
                            "backgroundColor": "#DFFFDF",
                            "action": {
                                "type": "message",
                                "label": "長興",
                                "text": se + "長興"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "T2",
                                    "size": "30px",
                                    "weight": "bold"
                                }
                            ],
                            "justifyContent": "center",
                            "alignItems": "center",
                            "height": "80px",
                            "borderWidth": "normal",
                            "borderColor": "#000000",
                            "cornerRadius": "xxl",
                            "width": "110px",
                            "margin": "md",
                            "backgroundColor": "#D2E9FF",
                            "action": {
                                "type": "message",
                                "label": "T2",
                                "text": se + "T2"
                            }
                        }
                    ],
                    "justifyContent": "center",
                    "alignItems": "center",
                    "height": "100px"
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
                                    "text": "山鼻",
                                    "size": "30px",
                                    "weight": "bold"
                                }
                            ],
                            "justifyContent": "center",
                            "alignItems": "center",
                            "height": "80px",
                            "borderWidth": "normal",
                            "borderColor": "#000000",
                            "width": "110px",
                            "cornerRadius": "xxl",
                            "backgroundColor": "#FFD2D2",
                            "action": {
                                "type": "message",
                                "label": "山鼻",
                                "text": se + "山鼻"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "廠辦",
                                    "size": "30px",
                                    "weight": "bold"
                                }
                            ],
                            "justifyContent": "center",
                            "alignItems": "center",
                            "height": "80px",
                            "borderWidth": "normal",
                            "borderColor": "#000000",
                            "width": "110px",
                            "cornerRadius": "xxl",
                            "margin": "md",
                            "backgroundColor": "#E2C2DE",
                            "action": {
                                "type": "message",
                                "label": "廠辦",
                                "text": se + "廠辦"
                            }
                        }
                    ],
                    "justifyContent": "center",
                    "alignItems": "center",
                    "height": "100px"
                },
                {
                    "type": "separator",
                    "margin": "xxl"
                }
            ],
            "background": {
                "type": "linearGradient",
                "angle": "0deg",
                "startColor": "#D1E9E9",
                "endColor": "#FFFFFF"
            }
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "重新查詢",
                            "weight": "bold",
                            "size": "xl",
                            "align": "center"
                        }
                    ],
                    "action": {
                        "type": "message",
                        "label": "research",
                        "text": "路線選擇"
                    }
                }
            ],
            "background": {
                "type": "linearGradient",
                "angle": "0deg",
                "startColor": "#D1E9E9",
                "endColor": "#D1E9E9"
            }
        }
    }
    return contents
