import json

import allure
import pytest

from requests_study.mtxshop_apis import buyer_login, buy_now, create_trade, add_cart


# @pytest.fixture(scope="session", autouse=False)
# def buyer_login_fixture():
#     buyer_login()
#     print("fixture函数执行")

@allure.epic("码同学微服务商城项目")
@allure.feature("买家服务接口")
@allure.story("创建交易接口正向用例")
# @pytest.mark.usefixtures("buyer_login_fixture")
class TestCreateTrade:
    # def test_create_trade(self):
    #     buyer_login()
    #     buy_now()
    #     resp = create_trade(client="PC", way="BUY_NOW")
    #     assert resp.status_code == 200
    #
    # def test_create_trade1(self):
    #     buyer_login()
    #     add_cart()
    #     resp = create_trade(client="PC", way="CART")
    #     assert resp.status_code == 200
    #
    # def test_crate_trade2(self):
    #     buyer_login()
    #     buy_now()
    #     resp = create_trade(client="PC", way="BUY_NOW")
    #     assert resp.status_code == 200
    #
    # def test_create_trade3(self):
    #     buyer_login()
    #     add_cart()
    #     resp = create_trade(client="PC", way="CART")
    #     assert resp.status_code == 200

    client_data = ["PC", "WAP", "NATIVE", "REACT", "MINI"]
    way_data = ["BUY_NOW", "CART"]

    @pytest.mark.parametrize("client", client_data)
    @pytest.mark.parametrize("way", way_data)
    # 上面参数组织好了，接下来定义测试用例
    def test_create_trade(self, client, way, buyer_login_fixture, db_ini):
        allure.dynamic.title(f"创建交易时{client} + {way}")
        # buyer_login()
        # 如果way中传入的参数是BUY_NOW,就调用立即购买接口
        # 如果way中传入的参数是CART，就调用添加购物车接口

        if way == "BUY_NOW":
            buy_now()
        else:
            add_cart()
        resp = create_trade(client=client, way=way)
        resp_sku_id = resp.json()['order_list'][0]['sku_list'][0]['sku_id']
        resp_num = resp.json()['order_list'][0]['sku_list'][0]['num']

        assert resp.status_code == 200
        # 查询订单信息
        res = db_ini.select(f"select * from mtxshop_trade.es_order where member_id = {buyer_login_fixture} ORDER BY order_id DESC LIMIT 2 ")
        db_items_json = res[0]['items_json']
        db_items_json = json.loads(db_items_json)
        db_sku_id = db_items_json[0]['sku_id']
        db_num = db_items_json[0]['num']
        pytest.assume(resp_sku_id == db_sku_id, f"expect_result: {resp_sku_id}, actual_result: {db_sku_id}")
        pytest.assume(resp_num == db_num, f"expect_result: {resp_num}, actual_result: {db_num}")
    # 这部分的前置跟后置的处理先注释掉，用fixture函数来处理吧
    # def setup_method(self):
    #     buyer_login()
    #     print("这是类级别的前置")
    #
    # def teardown_method(self):
    #     print(f"这是类级别后置")

    # def test_token(self, get_token):  # 有返回值的token需要在测试用例参数中调用函数名称,这个函数名称在用例内部使用时就代表了返回值
    #     print(f"\n得到的token: {get_token}")
