from linebot.models import (TextSendMessage, ImageSendMessage, FlexSendMessage, LocationMessage)
from Module.flexModule import AtoB, three_page, four_page, video_test_page, transit_map, step_choice


def return_flex(alt_text, contents):
    return FlexSendMessage(alt_text=alt_text, contents=contents)


def return_img(original_content_url, preview_image_url):
    return ImageSendMessage(original_content_url=original_content_url, preview_image_url=preview_image_url)


def return_text(text):
    return TextSendMessage(text=text)


def return_locat(title, address, x, y):
    return LocationMessage(title=title, address=address, latitude=x, longitude=y)


mesDic = dict({"廠辦線": return_flex("廠辦線", AtoB("廠辦線", "【去程】EGAS > T2", "EGAS to T2",
                                                    "【回程】T2 > EGAS", "T2 to EGAS")),
               "EGAS to T2": return_flex("EGAS > T2", three_page("https://i.imgur.com/vmnJenZ.jpg", "廠辦1",
                                                                 "https://i.imgur.com/ga31aK5.jpg", "廠辦2",
                                                                 "https://i.imgur.com/c87o95S.jpg", "廠辦3")),
               "T2 to EGAS": return_flex("T2 > EGAS", three_page("https://i.imgur.com/yy6pf3C.jpg", "廠辦4",
                                                                 "https://i.imgur.com/iCr63se.jpg", "廠辦5",
                                                                 "https://i.imgur.com/hQm4bJR.jpg", "廠辦6")),
               "EGAS to T2(新)": return_flex("EGAS > T2(新)", four_page("https://i.imgur.com/HNMsYsL.jpg", "廠辦1(新)",
                                                                        "https://i.imgur.com/AQ4JjJQ.jpg", "廠辦2(新)",
                                                                        "https://i.imgur.com/fkif50U.jpg", "廠辦3(新)",
                                                                        "https://i.imgur.com/hbDO7pl.jpg",
                                                                        "廠辦4(新)")),
               "T2 to EGAS(新)": return_flex("T2 > EGAS(新)", four_page("https://i.imgur.com/vcVEDNs.jpg", "廠辦5(新)",
                                                                        "https://i.imgur.com/5rifrtL.jpg", "廠辦6(新)",
                                                                        "https://i.imgur.com/viIue0o.jpg", "廠辦7(新)",
                                                                        "https://i.imgur.com/eWTKvs0.jpg",
                                                                        "廠辦8(新)")),
               "EGASWalk": return_img("https://i.imgur.com/zeyrBUj.jpg", "https://i.imgur.com/zeyrBUj.jpg"),
               "T2Walk": return_img("https://i.imgur.com/Omr4t9w.jpg", "https://i.imgur.com/Omr4t9w.jpg"),
               "影片測試": return_flex("Video TEST",
                                       video_test_page("https://i.imgur.com/0xOfojx.png", "EGAS <-> A14a", "#a5a552",
                                                       "EGASWalk",
                                                       "https://youtu.be/i_LqwGNfAmM")),
               "影片測試2": return_flex("Video TEST",
                                        video_test_page("https://i.imgur.com/Lxu9u7L.png", "T2 <-> A13", "#9f4d95",
                                                        "T2Walk",
                                                        "https://youtu.be/r088JL-zitA")),
               "地點測試": return_locat("Test", "搭車點", 25.077169, 121.233441),
               "時刻表測試": return_flex("Transit_Test", transit_map())})


def chk_mes(ukey):
    if ukey in mesDic:
        return mesDic[ukey]
    elif "路線選擇" == ukey:
        return return_flex("step choice", step_choice("-", "start/"))
    elif "start" in ukey:
        sp_s = ukey.split("/")[1]
        return return_flex("start step", step_choice(sp_s, f"end:{sp_s}/"))
    else:
        return return_text("功能開發中!!")
