from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage)
from Module.flexModule import transit, AtoB, gigaPage, positionPage, carouselPage


def return_flex(alt_text, contents):
    return FlexSendMessage(alt_text=alt_text, contents=contents)


def return_img(original_content_url, preview_image_url):
    return ImageSendMessage(original_content_url=original_content_url, preview_image_url=preview_image_url)


def return_text(text):
    return TextSendMessage(text=text)


mesDic = dict({"廠辦線": return_flex("廠辦線", AtoB("廠辦線", "【去程】EGAS to T2", "EGAS to T2",
                                                    "【回程】T2 to EGAS", "T2 to EGAS")),
               "EGAS to T2": return_img("https://i.imgur.com/tqTCfWQ.jpg", "https://i.imgur.com/tqTCfWQ.jpg"),
               "T2 to EGAS": return_img("https://i.imgur.com/NPhQEHk.jpg", "https://i.imgur.com/NPhQEHk.jpg"),
               "長興線": return_img("https://i.imgur.com/tHiDkuI.jpg", "https://i.imgur.com/tHiDkuI.jpg"),
               "A15線": return_img("https://i.imgur.com/3CM7rat.jpg", "https://i.imgur.com/3CM7rat.jpg"),
               "T2walk": return_flex("T2行走路線", carouselPage()),
               "EGASwalk": return_flex("EGAS行走路線", positionPage()),
               "information": return_flex("版型", gigaPage())})


def chk_mes(ukey):
    if ukey in mesDic:
        return mesDic[ukey]
    else:
        return return_text("功能開發中!!")
