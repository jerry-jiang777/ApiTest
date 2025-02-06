import requests


session = requests.session()  # 后期接口调用全部使用session对象进行调用,cookie就被自动关联了
token = ""


def login(username='cici', password='d92652d4522c9bc175f9ef5bbc862a9f'):
    url = 'http://59.36.173.55:7002/passport/login'
    data = {
        "username": username,
        "password": password,
        "uuid": "518ebdb0-d3e7-11ef-bc9c-bffaa05dff42",
        "captcha": "1512"
    }
    resp = session.request(method="post", url=url, data=data)
    # print(resp.text)
    # print(resp.status_code)
    # print(resp.json())
    if resp.status_code == 200:
        global token
        token = resp.json()["access_token"]
        print(f"登录接口调用结果: {resp.status_code}, {type(resp.status_code)}")
        print(resp.text)
        # print(f"token = {token}")
        return resp
    else:
        print(f"登录失败状态码:{resp.status_code}, {type(resp.status_code)}")
        print(f"登录失败")
        return resp.status_code


def set_address(address_id):
    url = f"http://59.36.173.55:7002/trade/checkout-params/address-id/{address_id}"
    headers = {
        "Authorization": token
    }
    resp = session.request(method="post", url=url, headers=headers)
    print(f"设置收货地址接口调用结果: {resp.status_code}")
    print(resp.text)
    return resp


def set_payType(payment_type="COD"):
    url = f"http://59.36.173.55:7002/trade/checkout-params/payment-type"
    headers = {
        "Authorization": token
    }
    data = {
        "payment_type ": "COD"
    }
    resp = session.request(method="post", url=url, data=data, headers=headers)
    print(f"支付方式接口调用结果: {resp.status_code}")
    print(resp.text)
    return resp

# 下单涉及到的接口
# 1. 设置订单收货地址的接口->支付方式接口->立即购买->创建交易接口


if __name__ == "__main__":
    login()
    # set_address(address_id=15985)
    # set_payType()
