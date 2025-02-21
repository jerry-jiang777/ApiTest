import allure

from requests_study.mtxshop_apis import buyer_login


@allure.epic("码同学全栈接口项目")
@allure.feature("cookie案例")
@allure.story("登陆接口各项用例")
@allure.title("买家登录成功")
def test_login_success():
    # 调用目标接口,作为测试数据传入
    resp = buyer_login(username="cici", password="d92652d4522c9bc175f9ef5bbc862a9f")
    # 断言
    status_code = resp.status_code
    assert status_code == 200  # 状态码断言
    # 针对接口响应中的核心字段校验
    # code = resp.json()["code"]  # 从响应体中获取code值

    # assert code == "0"
    # message = resp.json()["message"]  # 从响应体中获取message的值
    # assert message == "success"
    # 如何获取整体响应数据是否正确呢
    # text = resp.text
    # assert text == '{"uid":7778611,"username":"cici","nickname":"cici","access_token":"eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjc3Nzg2MTEsInN1YiI6IkJVWUVSIiwicm9sZXMiOlsiQlVZRVIiXSwiZXhwIjoxNzM5MzU0OTQzLCJ1dWlkIjpudWxsLCJ1c2VybmFtZSI6ImNpY2kifQ.PqGghm8bKwB8f1DjbX1TODpjsWhFc0t_yV8Q0AqJ8BKV29fb1ZN5m3sxMtRGShzWWEYvLB5TZKlApUScORpaEQ","refresh_token":"eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjc3Nzg2MTEsInN1YiI6IkJVWUVSIiwicm9sZXMiOlsiQlVZRVIiXSwiZXhwIjoxNzM5MzU1NTQzLCJ1dWlkIjpudWxsLCJ1c2VybmFtZSI6ImNpY2kifQ.tnOeIXnFd0rRa8UC_ciec31TomoAK7-3tXYe6vzIVvDtq3Q9qF7Utmx89IBBvB7enNKFiRnzXWez1q9Y2LYyvg","face":null}'
