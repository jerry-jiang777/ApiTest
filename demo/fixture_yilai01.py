import pytest


@pytest.fixture
def db_connection():
    print(f"\n连接数据库")
    return "Database Connected"


@pytest.fixture
def user_data(db_connection):
    print(f"\n 获取用户数据")
    return {"db": db_connection, "user": "test_user"}


@pytest.fixture
def test_user(user_data):
    print(f"测试用户数据: {user_data}")
    assert user_data['db'] == 'Database Connected'
