# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : cookie_study.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/8 16:31
# @Copyright: 北京码同学
import requests

# 该session对象可以帮助我们自动管理和传递cookie
# 后续的接口调用都必须使用session对象发起
session = requests.session()


def login(username='shamo', password='123456'):
    url = "http://59.36.173.55:7002/pinter/bank/api/login"
    data = {
        "userName": username,
        "password": password
    }
    # resp = requests.post(url=url,data=data)
    # resp = session.post(url=url,data=data)
    resp = session.request(method='post', url=url, data=data)
    # 获取响应状态码
    status_code = resp.status_code
    print(f"响应状态码是:{status_code}")
    # 获取响应body体数据，以字符串方式获取，得到的结果就是一个字符串
    text = resp.text
    print(f'响应数据字符串形式是:{text}')
    # 如果响应数据本身是一个json形式的数据，那么还可以以json格式获取
    resp_json = resp.json()  # 得到的结果有可能是字典也有可能是列表
    print(f'响应数据json形式是:{resp_json}')
    print(f'响应头信息是:{resp.headers}')
    return resp


def query(username='shamo'):
    url = "http://82.156.74.26:9088/pinter/bank/api/query"
    params = {
        "userName": username
    }
    # resp = requests.get(url=url,params=params)
    # resp = session.get(url=url, params=params)
    resp = session.request(method='get', url=url, params=params)
    # 获取响应状态码
    status_code = resp.status_code
    print(f"响应状态码是:{status_code}")
    # 获取响应body体数据，以字符串方式获取，得到的结果就是一个字符串
    text = resp.text
    print(f'响应数据字符串形式是:{text}')
    # 如果响应数据本身是一个json形式的数据，那么还可以以json格式获取
    resp_json = resp.json()  # 得到的结果有可能是字典也有可能是列表
    print(f'响应数据json形式是:{resp_json}')
    print(f'响应头信息是:{resp.headers}')


if __name__ == '__main__':
    login()
    query()
