import requests


def get():
    # 接口地址
    url = "http://59.36.173.55:7000/pages/article-categories"
    # 接口请求头信息
    # 接口请求参数s
    parser = {
        "category_type": "HELP"
    }
    # resp实际上包含了响应的很多信息,响应头信息, 响应状态码, 响应body体数据
    resp = requests.get(url=url, params=parser)
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
    get()
