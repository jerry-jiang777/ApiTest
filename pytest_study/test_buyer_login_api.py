# 以类的方式编写测试用例
from requests_study.mtxshop_apis import login


class TestBuyerLogin:

    # 在测试类中不能存在__init__方法
    # 在测试类中以test_开头的的方法代表一条测试用例

    def test_login_success(self):
        resp = login()
        # 断言
        assert resp.json()["username"] == "cici"
        assert resp.json()["nickname"] == "cici"
        # 一般在编写测试用例的时候推荐只使用一种方式编写类 要么只用类的方式编写测试用例 要么只用函数编写测试用例
        # python中默认的测试框架是unittest框架而不是pytest框架执行用例，想使用pytest执行的话需要做一些设置才行
