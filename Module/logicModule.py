import sqlite3
import pandas as pd
import datetime


def route_control(route_start, route_end):
    conn = sqlite3.connect('Data/TestDB.db')
    res = pd.read_sql(f"SELECT * FROM ROUTEINFO", conn)
    conn.close()
    d = {}
    e = {}
    ans = {}
    now = datetime.datetime.now()
    now_ms = (now.hour * 60) + now.minute
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
    res = [{
        "type": "text",
        "text": "長興01",
        "weight": "bold",
        "size": "30px"
    }, {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "alignItems": "center",
        "margin": "xl"}]
    body_contents = []
    rc = route_control(route_start, route_end)
    for rci in range(len(rc)):
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
    return res

