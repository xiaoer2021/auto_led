# -*- coding: utf-8 -*-
import datetime
import json
import time
import requests
import schedule

session = requests.session()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}
data = {
    'username': 'ledauto',
    'password': 'ledauto'
}
url = 'http://sw.gdshiwei.cn/apm-web/a/login'
esp = session.post(url, data=data, headers=headers)
print(esp.text)

list_id = {
    '245dfc6469f847cd8a47cadcaaac101021',
    '245dfc6469f347cd8abcca6b2fac101021',
    '245dfc6469f947cd8a47821b2aac101021',
    '245dfc646d5747cd8afd4fe5ceac101021',
    '245dfc6469f447cd8abcc7a10bac101021',
    '245dfc6469f747cd8ac11724b8ac101021',
    '245dfc63f87e47cd8abcc8ceddac101021'
}
# 开机状态
data = {
    'terminalIds': list_id,
    'password': '0',
    'power': '1'
}
# 休眠状态
data2 = {
    'terminalIds': list_id,
    'password': '0',
    'power': '2'
}


# 上班时间
def working():
    work_url = 'http://sw.gdshiwei.cn/apm-web/a/api/terminalSet/terminalSet'
    work = session.post(work_url, data=data)
    print("上班啦")


# 下班时间
def clock_off():
    holidays_url = 'http://sw.gdshiwei.cn/apm-web/a/api/terminalSet/terminalSet'
    hd = session.post(holidays_url, data=data2)
    print("下班啦")


# 公司假期时间
def holidays():
    holidays_url = 'http://sw.gdshiwei.cn/apm-web/a/api/terminalSet/terminalSet'
    hd = session.post(holidays_url, data=data2)
    print("今天是假期噢")


def time_conlose():
    # 假期公告时间
    week = {
        '2022-11-11',
        '2022-11-08',
        '2022-11-09',
        '2022-11-07',
        '2022-11-16',
    }
    # 判断当下时间，格式化时间格式为 年-月-日
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    # 遍历一遍week数据，判断当下时间是否在week里
    if now in week:
        print("放假时间")
        return holidays()
    else:
        print("上班啦！")
        return working()


# 开机
schedule.every().day.at("08:55").do(working)
# 关机
schedule.every().day.at("12:00").do(clock_off)
# 开机
schedule.every().day.at("13:30").do(working)
# 关机
schedule.every().day.at("20:00").do(clock_off)

while True:
    schedule.run_pending()
#
# url = 'http://sw.gdshiwei.cn/apm-web/a/api/terminalSet/getRltMonitor?'
# req = session.get(url)
# req_json = req.json()
# print(req_json)
#

# 登录凭证
# headers_1 = {
#     'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
# }
# # 获得cookie值
# resp = requests.get('http://sw.gdshiwei.cn/apm-web/servlet/validateCodeServlet?12', headers=headers_1)
# cook = resp.headers.get('set-cookie')
# cookies = cook.split(';')[0]
# print(cookies)
#
# # 登录接口
# login_url1 = 'http://sw.gdshiwei.cn/apm-web/a/login'
# login_url2 = 'http://sw.gdshiwei.cn/apm-web/a/loginSuccess'
# # 传参
#
#
# # 第一步登录验证
# headers_2 = {
#     'Accept': 'application/json, text/plain, */*',
#     'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Cookie': cookies + ';language=zh_CN;',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
# }
# # 用于第二步验证
# # headers_3 = {
# #     'Accept': 'application/json, text/plain, */*',
# #     'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
# # }
# print(headers_2)
# resp_2 = requests.post(login_url2, headers=headers_2, data=data)
# print(resp_2.text)

# # 设备ID列表
# led_list = {
#     '245dfc6469f847cd8a47cadcaaac101021'
#     '245dfc6469f947cd8a47821b2aac101021'
#     '245dfc646d5747cd8afd4fe5ceac101021'
#     '245dfc6469f447cd8abcc7a10bac101021'
#     '245dfc6469f747cd8ac11724b8ac101021'
#     '245dfc63f87e47cd8abcc8ceddac101021'
#     '245dfc6469f347cd8abcca6b2fac101021'
# }
# # 传参 开机状态
#

#
# def login():
#     resp = requests.post(login_url, data=parameter, headers=headers_2, )
#     print(resp)
#
# #
# # post请求进行登录
# # post请求进行控制设备状态码
# # req = requests.post('http://sw.gdshiwei.cn/apm-web/a/api/terminalSet/terminalSet',headers=headers_2, data=data,)
# # print(req.text)
