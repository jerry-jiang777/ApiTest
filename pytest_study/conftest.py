from typing import List

import pytest

from db_study.db_util import DBUtil
from redis_study.redis_utils import RedisUtil
from requests_study.mtxshop_apis import buyer_login





def pytest_collection_modifyitems(items: List["Item"]):
    for item in items:
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope="session", autouse=True)
def buyer_login_fixture():
    resp = buyer_login()
    uid = resp.json()['uid']
    print("fixture函数执行")
    yield uid
    print(f"\n用例执行完成了,退出登录")


@pytest.fixture(scope="session", autouse=False)
def get_token():
    resp = buyer_login()
    buyer_token = resp.json()["access_token"]
    print(f"执行fixture函数")
    yield buyer_token  # 这里相当于返回值了。相当于return
    print(f"用例执行完成了,退出登录")


@pytest.fixture(scope="session",autouse=False)
def redis_ini():
    r = RedisUtil(host="59.36.173.55", pwd="mtx", port=6379)
    yield r


@pytest.fixture(scope="session", autouse=True)
def db_ini():
    db_util = DBUtil(
        host="59.36.173.55",
        user="mtxshop_test",
        password="mtxshamo",
        port=3306
                     )
    yield db_util
    db_util.close()
