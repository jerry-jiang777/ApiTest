import javaobj
import pytest
from requests_study.mtxshop_apis import set_payType


class TestSetPayTypeApi:
    def test_set_online(self, redis_ini):
        """验证支付方式用例"""
        resp = set_payType(payment_type='ONLINE')
        pytest.assume(resp.status_code == 200)
        # redis 数据断言 这里要redis断言要先连接redis数据库并拿数据，所有要初始化redis连接，引入redis_ini
        res = redis_ini.get("{CHECKOUT_PARAM_ID_PREFIX}_7778611")  # 确认收获地址的操作
        for key, value in res.items():
            key = javaobj.loads(key)
            if key == 'paymentType':
                value = javaobj.loads(value)
                value = value.constant
                print(f"{key}: {value}")
                break
        pytest.assume(value == "ONLINE", f"预期结果: ONLINE, 实际结果: {value}")

    def test_set_cod(self, redis_ini):
        """货到付款"""
        resp = set_payType(payment_type='COD')
        pytest.assume(resp.status_code == 200)
        # redis 数据断言 这里要redis断言要先连接redis数据库并拿数据，所有要初始化redis连接，引入redis_ini
        res = redis_ini.get("{CHECKOUT_PARAM_ID_PREFIX}_7778611")  # 确认收获地址的操作
        for key, value in res.items():
            key = javaobj.loads(key)
            if key == 'paymentType':
                value = javaobj.loads(value)
                value = value.constant
                print(f"{key}: {value}")
                break
        pytest.assume(value == "COD", f"预期结果: ONLINE, 实际结果: {value}")

