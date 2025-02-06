# 以表单形式的post接口
# 以买家登录
import requests


def buyer_login():
    url = "http://59.36.173.55:7002/passport/login"
    header = {
        "Authorization":""
    }
    # 以表单参数形式
    data = {
        "username ": "shamo",
        "password": "",
        "captcha ": "1512",
        "uuid": "24576"
    }
    # 发起调用
    resp = requests.post(url=url, data=data,headers=header)
    # 获取响应状态码
    status_code = resp.status_code
    print(f"响应状态码是: {status_code}")
    # 获取响应body体数据, 以字符串形式获取,得到的结果就是一个字符串
    text = resp.text
    print(f"响应数据字符串形式是: {text}")
    # 如果响应数据是json形式的数据
    resp_json = resp.json()
    print(f"响应数据json形式的是: {resp_json}")
    print(f"响应的头信息是: {resp.headers}")


if __name__ == "__main__":
    buyer_login()
