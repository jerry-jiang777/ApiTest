import pytest


# @pytest.fixture
# def setup_data():
#     print(f"\n执行前置操作:初始化数据")
#     data = {"username": "test_user", "password": "123456"}
#     return data
#
#
# def test_login(setup_data):
#     print(f"使用数据{setup_data} 进行测试")
#     assert setup_data["username"] == "test_user"
# ====================================================
@pytest.fixture(scope="module")
def setup_module():
    print("\n[前置] 初始化数据库连接")
    db = {"connection": "MySQL"}
    yield db
    print("\n[后置] 关闭数据库连接")


def test_case1(setup_module):
    print(f"测试1 - {setup_module}")


def test_case2(setup_module):
    print(f"测试2 - {setup_module}")



