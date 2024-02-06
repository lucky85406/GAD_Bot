from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage)
from Module.flexModule import AtoB, rmenu_design


def return_flex(alt_text, contents):
    return FlexSendMessage(alt_text=alt_text, contents=contents)


def return_img(original_content_url, preview_image_url):
    return ImageSendMessage(original_content_url=original_content_url, preview_image_url=preview_image_url)


def return_text(text):
    return TextSendMessage(text=text)


mesDic = dict({"圖文選單": rmenu_design()})


def chk_mes(ukey):
    if ukey in mesDic:
        return mesDic[ukey]
    else:
        return return_text("功能開發中!!")
