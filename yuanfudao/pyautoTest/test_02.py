import pytest

def add(x,y):
    return x + y

def login(username,pwd):
    print("去服务器校验")

    if username == "abc" and pwd == "123":
        return "登录成功!!"
    else:
        return "登录失败!!"


def read_excel():
    return [(1,2),(3,4),(5,6),(7,8),(9,10)]

@pytest.mark.parametrize(["z"],[11,22])
@pytest.mark.parametrize(["x", "y"],read_excel())

def test_c(x,y,z):
    print("--test_c---")
    # assert 断言
    # assert False
    print("x的值为:", x)
    print("y的值为:", y)
    print("z的值为:", z)
    res = add(x,y)

    assert res == 7

def test_a():
    print("---test_a---")

    x = 5
    y = 1

    res = add(x+y)
    assert res != 6

def test_b():
    print("---test_b---")

    res = login("abc", "123")
    assert "登录成功" in res


def test_recursion_depth():
    with pytest.raises(ZeroDivisionError) as excinfo:
        # 预期会出现异常的代码
        1/0
    assert "division by zero" in str(excinfo.value)

