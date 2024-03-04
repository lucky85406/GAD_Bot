from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage, LocationMessage)
from Module.flexModule2 import profit_calculation, boss_item, choose_form


def return_flex(alt_text, contents):
    return FlexSendMessage(alt_text=alt_text, contents=contents)


def return_img(original_content_url, preview_image_url):
    return ImageSendMessage(original_content_url=original_content_url, preview_image_url=preview_image_url)


def return_text(text):
    return TextSendMessage(text=text)


def return_locat(title, address, x, y):
    return LocationMessage(title=title, address=address, latitude=x, longitude=y)


def chk_mes(uid, mes):
    if uid == "U61a0a5800e8265a3ad897623cfbc4e22" and mes == "收益":
        return [True, return_flex("計算收益", profit_calculation())]
    elif uid == "U61a0a5800e8265a3ad897623cfbc4e22" and mes == "BOSS":
        return [True, return_flex("項目表", boss_item())]
    elif uid == "U61a0a5800e8265a3ad897623cfbc4e22" and mes == "選擇":
        return [True, return_flex("選擇表", choose_form())]
    else:
        return [False, ""]
