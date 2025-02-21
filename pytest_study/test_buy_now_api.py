import allure
import javaobj
import pytest

from redis_study.redis_utils import RedisUtil
from requests_study.mtxshop_apis import buy_now


@allure.epic('码同学微服务商城项目')
@allure.feature("买家服务接口")
@allure.story("立即购买接口异常用例")
class TestBuyNow:
    test_data = [
        ["产品id不存在（这是测试用例名称）", 7781442131, 1, 500, '{"code":"004","message":"不合法"}'],
        ["num为0（这是测试用例名称）", 541, 0, 400, '{"code":"004","message":"购买数量必须大于0"}'],
        ["num为负数（这是测试用例名称）", 541, -1, 400, '{"code":"004","message":"购买数量必须大于0"}'],
        ["num超过库存（这是测试用例名称）", 541, 100000, 200, '']
    ]

    @allure.title("{casename}")
    @pytest.mark.parametrize("case_name, sku_id, num, except_code, except_body", test_data)
    # @pytest.mark.repeat(2)  # 装饰起该用例重复执行2次
    def test_buy_now(self, case_name, sku_id, num, except_code, except_body):
        """立即购买功能测试"""
        resp = buy_now(sku_id, num)
        # assert resp.status_code == except_code
        # assert resp.text == except_body
        pytest.assume(resp.status_code == except_code,
                      f"期望相应状态码: {except_code}, 实际响应状态码: {resp.status_code}")
        pytest.assume(resp.text == except_body, f"期望响应体: {except_body}, 实际响应体: {resp.text}")

    @allure.title("立即购买成功")
    def test_buy_now_success(self, redis_ini, buyer_login_fixture):
        resp = buy_now(sku_id=541, num=1)
        pytest.assume(resp.status_code == 200, f"期望值: 200, 实际结果: {resp.status_code}")
        # r = RedisUtil(host="59.36.173.55", pwd="mtx", port=6379)
        res = redis_ini.get(f"{{BUY_NOW_ORIGIN_DATA_PREFIX}}_{buyer_login_fixture}")
        res_obj = javaobj.loads(res)
        buy_now_object = res_obj[0]
        skuId = buy_now_object.__getattribute__("skuId")
        num = buy_now_object.__getattribute__("num")
        pytest.assume(skuId == 541, f"期望值: 541, 实际结果: {skuId}")
        pytest.assume(num == 1, f"期望值: 1, 实际结果: {num}")

