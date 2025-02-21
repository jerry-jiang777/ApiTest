import allure


# 查询余额之前需要完成登录，这里可能会有多条查询余额的用例
def setup_function():
    print(f"\n前置操作")


def teardown_function():
    print(f"\n后置操作")


@allure.epic("码同学全栈接口项目")
@allure.feature("cookie案例")
@allure.story("登陆接口各项用例")
@allure.title("登陆成功")
def test_01():
    print("\n测试用例1开始执行")
    print(f"1111")
    print("测试用例1执行完成了")


@allure.epic("码同学全栈接口项目")
@allure.feature("cookie案例")
@allure.story("登陆接口各项用例")
@allure.title("登录用户名为空")
def test_02():
    print("\n测试用例2开始执行")
    print(f"2222")
    print("测试用例2执行完成了")
