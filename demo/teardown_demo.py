import pytest


@pytest.fixture
def setup_and_teardown():
    print(f"\n[前置] 连接数据库")
    con = {"db": "MySQL", "status": "connected"}
    yield con
    print(f"\n[后置] 关闭数据库")


def test_database(setup_and_teardown):
    print(f"数据库连接状态: {setup_and_teardown['status']}")
    assert setup_and_teardown['status'] == 'connected'
