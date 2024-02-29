import sqlite3
import pandas as pd
import datetime
import pytz


def route_control(route_start, route_end):
    conn = sqlite3.connect('Data/TestDB.db')
    res = pd.read_sql(f"SELECT * FROM ROUTEINFO", conn)
    conn.close()
    d = {}
    e = {}
    ans = {}
    now = datetime.datetime.now(pytz.timezone("Asia/Taipei"))
    now_ms = (now.hour * 60) + now.minute
    for i in range(len(res)):
        for ri in range(1, 8):
            route_i = "ROUTE" + str(ri)
            if res.iloc[i][route_i] != "-":
                sp_st = res.iloc[i][route_i].split("/")[1]
                st_ms = int(sp_st[0:2]) * 60 + int(sp_st[2:4])
                if route_start in res.iloc[i][route_i] and ri != 7:
                    for li in range(ri + 1, 8):
                        route_li = "ROUTE" + str(li)
                        if route_end in res.iloc[i][route_li]:
                            sp_r1 = res.iloc[i]["ROUTE1"].split("/")[1]
                            r1_ms = int(sp_r1[0:2]) * 60 + int(sp_r1[2:4])
                            if now_ms <= st_ms:
                                d[r1_ms] = res.iloc[i]
                            else:
                                e[r1_ms] = res.iloc[i]

                    break

    if d:
        sort_key = sorted(d.keys())
        if len(d) >= 3:
            for ai in range(3):
                ans[ai] = d[sort_key[ai]]
        elif 0 < len(d) < 3:
            for ai in range(len(sort_key)):
                ans[ai] = d[sort_key[ai]]
    elif e:
        sort_key = sorted(e.keys())
        if len(e) >= 3:
            for ai in range(3):
                ans[ai] = e[sort_key[ai]]
        elif 0 < len(e) < 3:
            for ai in range(len(sort_key)):
                ans[ai] = e[sort_key[ai]]

    return ans


def combin_route(route_start, route_end):
    buddle_dict = []
    rc = route_control(route_start, route_end)
    for rci in range(len(rc)):
        body_contents = []
        one_buddle = {
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
                                "type": "text",
                                "text": "From",
                                "weight": "bold",
                                "size": "40px",
                                "color": "#6C6C6C",
                                "style": "italic"
                            }, {
                                "type": "text",
                                "text": route_start,
                                "size": "30px",
                                "weight": "bold",
                                "align": "center"
                            }
                        ],
                        "width": "250px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "↓",
                                "size": "35px",
                                "align": "center",
                                "color": "#FF0000"
                            }
                        ],
                        "width": "250px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "To",
                                "weight": "bold",
                                "size": "40px",
                                "color": "#6C6C6C",
                                "style": "italic"
                            },
                            {
                                "type": "text",
                                "text": route_end,
                                "size": "30px",
                                "weight": "bold",
                                "align": "center"
                            }
                        ],
                        "margin": "xxl",
                        "width": "250px"
                    },
                    {
                        "type": "separator",
                        "color": "#000000"
                    }
                ],
                "backgroundColor": "#B3D9D9"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": []
                    }
                ]
            }
        }
        res = [
            {
                "type": "box",
                "layout": "horizontal",
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
                                        "text": "路線：",
                                        "size": "23px",
                                        "weight": "bold"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": rc[rci]["ROUTEGROUP"],
                                        "size": "20px",
                                        "weight": "bold"
                                    }
                                ]
                            }
                        ],
                        "width": "140px"
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
                                        "text": "備註：",
                                        "size": "23px",
                                        "weight": "bold"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": rc[rci]["ROUTENOTE"],
                                        "size": "20px",
                                        "weight": "bold"
                                    }
                                ]
                            }
                        ],
                        "justifyContent": "flex-end",
                        "width": "140px",
                        "margin": "xxl"
                    }
                ]
            },
            {
                "type": "text",
                "text": rc[rci]["ROUTEITEM"],
                "weight": "bold",
                "size": "25px",
                "margin": "15px"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "alignItems": "center",
                "margin": "xl"}]
        route = [rc[rci][i] for i in ["ROUTE1", "ROUTE2", "ROUTE3", "ROUTE4", "ROUTE5", "ROUTE6", "ROUTE7"] if
                 rc[rci][i] != "-"]
        chk = 0
        for rti in range(len(route)):
            sp_route = route[rti].split("/")
            scolor = "#0066CC"
            tcolor = "#000000"
            if chk == 0 and sp_route[0] == route_start:
                scolor = "#FF2D2D"
                tcolor = "#FF2D2D"
                chk = 1
            elif chk == 1 and sp_route[0] == route_end:
                scolor = "#01B468"
                tcolor = "#01B468"
                chk = 2

            body_dict = {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": sp_route[0],
                        "size": "23px",
                        "color": tcolor
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "width": "15px",
                        "height": "15px",
                        "borderWidth": "medium",
                        "borderColor": scolor,
                        "cornerRadius": "xxl",
                        "alignItems": "center",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": f"{sp_route[1][0:2]}:{sp_route[1][2:4]}",
                        "size": "20px",
                        "margin": "md",
                        "color": tcolor
                    }
                ],
                "alignItems": "center",
                "width": "150px"
            }
            body_contents.append(body_dict)
            if rti + 1 < len(route):
                body_contents.append({
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "borderWidth": "light",
                    "borderColor": "#7B7B7B",
                    "height": "30px"
                })
        res[2]["contents"] = body_contents
        one_buddle["body"]["contents"][0]["contents"] = res
        buddle_dict.append(one_buddle)
    return buddle_dict


print(combin_route("T2", "廠辦"))
