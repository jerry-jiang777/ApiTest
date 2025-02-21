import pytest


@pytest.fixture
def setup_data():
    print(f"\n执行前置操作:初始化数据")
    data = {"username": "test_user", "password": "123456"}
    return data


def test_login(setup_data):
    print(f"使用数据{setup_data} 进行测试")
    assert setup_data["username"] == "test_user"


