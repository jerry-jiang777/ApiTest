# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : mtxshop_apis.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2023/7/8 16:40
# @Copyright: 北京码同学


import requests

token = ""

# 该session对象可以帮助我们自动管理和传递cookie
# 后续的接口调用都必须使用session对象发起
session = requests.session()


def buyer_login(username='cici', password='d92652d4522c9bc175f9ef5bbc862a9f'):
    url = 'http://59.36.173.55:7002/passport/login'
    headers = {
        "Authorization": ""
    }
    # 以表单参数方式
    data = {
        "username": username,
        "password": password,
        "captcha": "1512",
        "uuid": "a9957d60-e76e-11ef-996d-91510b05d05f"
    }
    # 发起调用
    # resp = requests.post(url=url,data=data,headers=headers)
    resp = session.request(method='post', url=url, data=data, headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f"\n登录响应状态码是:{status_code}")
    text = resp.text
    print(f"登陆成功返回的text格式数据为: {text}")
    # 如果响应数据本身是一个json形式的数据，那么还可以以json格式获取
    resp_json = resp.json()  # 得到的结果有可能是字典也有可能是列表
    print(f'响应数据json形式是:{resp_json}')
    # 提取响应结果中的access_token
    global token
    if status_code == 200:
        token = resp_json['access_token']
    return resp


# 下单的动作涉及到接口有
# 设置订单收货地址接口-->设置支付方式接口-->立即购买接口-->创建交易接口
def set_address(address_id):
    url = f'http://59.36.173.55:7002/trade/checkout-params/address-id/{address_id}'
    headers = {
        "Authorization": token
    }
    # 发起调用
    resp = session.request(method='post', url=url, headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f"设置收货地址响应状态码是:{status_code}")
    print(f'响应数据字符串形式:{resp.text}')
    # resp_json = resp.json() # 得到的结果有可能是字典也有可能是列表
    # print(f'响应数据json形式是:{resp_json}')
    return resp


def set_payType(payment_type='COD'):
    url = f'http://59.36.173.55:7002/trade/checkout-params/payment-type'
    headers = {
        "Authorization": token
    }
    data = {
        "payment_type": payment_type
    }
    resp = session.request(method='post', url=url, data=data, headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f"设置支付方式响应状态码是:{status_code}")
    print(f'响应数据字符串形式:{resp.text}')
    return resp


def buy_now(sku_id=541, num=1):
    """立即购买接口"""
    url = f'http://59.36.173.55:7002/trade/carts/buy'
    headers = {
        "Authorization": token
    }
    data = {
        "sku_id": sku_id,  # sku_id代表是商品的产品id，注意不是商品id，可以去查库在mtxshop_goods库的es_goods_sku表
        "num": num,
        "activity_id": ""
    }
    resp = session.request(method='post', url=url, data=data, headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f"\n立即购买操作响应状态码是:{status_code}")
    print(f'响应数据字符串形式:{resp.text}')
    return resp


def add_cart(sku_id=541, num=1):
    """添加购物车接口"""
    url = f'http://59.36.173.55:7002/trade/carts'
    headers = {
        "Authorization": token
    }
    data = {
        "sku_id": sku_id,  # sku_id代表是商品的产品id，注意不是商品id，可以去查库在mtxshop_goods库的es_goods_sku表
        "num": num,
        "activity_id": ""
    }
    resp = session.request(method='post', url=url, data=data, headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f"响应状态码是:{status_code}")
    print(f'响应数据字符串形式:{resp.text}')
    return resp


def create_trade(client='PC', way='BUY_NOW'):
    url = f'http://59.36.173.55:7002/trade/create'
    headers = {
        "Authorization": token
    }
    data = {
        "client": client,
        "way": way
    }
    resp = session.request(method='post', url=url, data=data, headers=headers)
    # 获取响应状态码
    status_code = resp.status_code
    print(f"提交订单操作响应状态码是:{status_code}")
    print(f'提交订单响应数据字符串形式:{resp.text}')
    return resp


if __name__ == '__main__':
    buyer_login()
    # set_address(address_id=15985)
    # set_payType()
    # buy_now()
    # create_trade()
