import pytest

# @pytest.fixture(param=[1,2,3])
# def init_data(request):
#     print("init_data:",request.param)
#     return request.param
def read_json():
    data=[
        {"user":"asd","pwd":"1234566"},
        {"user":"dfgg","pwd":"123456556"},
        {"user":"asddffd","pwd":"123dfg4566"},
        {"user":"asdjhgg","pwd":"1234566.."},
        {"user":"asdeggd","pwd":"1234566666"}
    ]
    return data

@pytest.fixture(params=read_json())
def login(request):
    print("login的内容是：",request.param)
    yield  request.param

    print("这是回收的代码")

def test_01(login):
    print("用户名是",login["user"])
    print("密码是", login["pwd"])


