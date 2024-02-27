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
    print(now)
    for i in range(len(res)):
        for ri in range(1, 8):
            route_i = "ROUTE" + str(ri)
            if res.iloc[i][route_i] != "-":
                sp_st = res.iloc[i][route_i].split("/")[1]
                st_ms = int(sp_st[0:2]) * 60 + int(sp_st[2:4])
                if route_start in res.iloc[i][route_i]:
                    for li in range(ri, 8):
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
                                "weight": "bold"
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
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "↓",
                                "size": "35px",
                                "align": "center",
                                "color": "#FF0000"
                            }
                        ]
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
                                "weight": "bold"
                            }
                        ],
                        "margin": "xxl"
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
                                        "size": "25px",
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
                                ],
                                "offsetEnd": "10px",
                                "offsetTop": "3px"
                            }
                        ],
                        "width": "170px"
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
                                        "size": "25px",
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
                                ],
                                "offsetTop": "3px",
                                "offsetEnd": "10px"
                            }
                        ],
                        "justifyContent": "flex-end",
                        "width": "160px",
                        "margin": "10px"
                    }
                ]
            },
            {
                "type": "text",
                "text": rc[rci]["ROUTEITEM"],
                "weight": "bold",
                "size": "30px"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "alignItems": "center",
                "margin": "xl"}]
        route = [rc[rci][i] for i in ["ROUTE1", "ROUTE2", "ROUTE3", "ROUTE4", "ROUTE5", "ROUTE6", "ROUTE7"] if
                 rc[rci][i] != "-"]
        for rti in range(len(route)):
            sp_route = route[rti].split("/")
            body_dict = {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": sp_route[0],
                        "size": "26px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "width": "15px",
                        "height": "15px",
                        "borderWidth": "medium",
                        "borderColor": "#0066CC",
                        "cornerRadius": "xxl",
                        "alignItems": "center",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": f"{sp_route[1][0:2]}:{sp_route[1][2:4]}",
                        "size": "22px",
                        "margin": "md"
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
        res[1]["contents"] = body_contents
        one_buddle["body"]["contents"][0]["contents"] = res
        buddle_dict.append(one_buddle)
    return buddle_dict
