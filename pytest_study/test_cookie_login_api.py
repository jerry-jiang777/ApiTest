from requests_study.mtxshop_apis import buyer_login
import allure
import pytest

test_data = [
    ["cici", "d92652d4522c9bc175f9ef5bbc862a9f", 200],
    ["", "d92652d4522c9bc175f9ef5bbc862a9f", 400],
    ["cici", "", 400]
]


@allure.epic("码同学全栈接口项目")
@allure.feature("cookie案例")
@allure.story("登陆接口各项用例")
@allure.title("买家登录成功")
@pytest.mark.parametrize("username, password, exception_res", test_data)
def test_login_success(username, password, exception_res):
    resp = buyer_login(username=username, password=password)
    status_code = resp.status_code
    assert status_code == exception_res


@allure.epic("码同学全栈接口项目")
@allure.feature("cookie案例")
@allure.story("登录接口各项用例")
@allure.title("买家用户名为空")
# @pytest.mark.flaky(reruns=2)
def test_login_username_is_null():
    resp = buyer_login(username='', password='d92652d4522c9bc175f9ef5bbc862a9f')
    status_code = resp.status_code
    assert status_code == 400


@allure.epic("码同学全栈接口项目")
@allure.feature("cookie案例")
@allure.story("登陆接口各项用例")
@allure.title("买家登录密码为空")
def test_login_password_is_null():
    resp = buyer_login(username='cici', password='')
    status_code = resp.status_code
    assert status_code == 400
