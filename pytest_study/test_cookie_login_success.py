from requests_study.mtxshop_apis import login

def test_login_success():
    # 调用目标接口,作为测试数据传入
    resp = login(username="cici", password="cici321654")
    # 断言
    status_code = resp.status_code
    assert status_code == 200  # 状态码断言
    # 针对接口响应中的核心字段校验
    # code = resp.json()["code"]  # 从响应体中获取code值

    # assert code == "0"
    # message = resp.json()["message"]  # 从响应体中获取message的值
    # assert message == "success"
    # 如何获取整体响应数据是否正确呢
    text = resp.text
    assert text == '{"uid":7778611,"username":"cici","nickname":"cici","access_token":"eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjc3Nzg2MTEsInN1YiI6IkJVWUVSIiwicm9sZXMiOlsiQlVZRVIiXSwiZXhwIjoxNzM3NDQwODk5LCJ1dWlkIjpudWxsLCJ1c2VybmFtZSI6ImNpY2kifQ.ceFAon4Zf-OIgZul1fqAbzbb0LPJrA8tabTYXJS0lKdrTXsEDTszy0T8Z4oFqM7ITnv1XuNE2upivumgb3-DwQ","refresh_token":"eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjc3Nzg2MTEsInN1YiI6IkJVWUVSIiwicm9sZXMiOlsiQlVZRVIiXSwiZXhwIjoxNzM3NDQxNDk5LCJ1dWlkIjpudWxsLCJ1c2VybmFtZSI6ImNpY2kifQ.7ZJHlzIbuT-FyvW9Qvc8_HOTSaKK_uxgQqsO3dMqyP4zxaPTW7iUaSR16HfaQUKtILEKRT8my_bW6oPKNJGwIg","face":null}'
