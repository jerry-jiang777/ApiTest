import pytest

from requests_study.mtxshop_apis import login

test_data = [
    ["cici", "d92652d4522c9bc175f9ef5bbc862a9f", 200],
    ["ci", "d92652d4522c9bc175f9ef5bbc862a9f", 500],
    ["cici", "d92652d4522c9bc175f9ef5bbc862a910", 500],
    ["cicix", "d92652d4522c9bc175f9ef5bbc862a9fxx", 500]
]


@pytest.mark.parametrize("username, passwprd, except_code", test_data)
def test_login(username, passwprd, except_code):
    resp = login(username, passwprd)
    assert resp.status_code == except_code
