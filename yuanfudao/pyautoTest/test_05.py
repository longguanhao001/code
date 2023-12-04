import pytest

@pytest.fixture()

def before():
    print("我运行了")
    return "香蕉"
@pytest.fixture()
def after(before):
    print("呵呵呵")
    return before, "苹果"

def test_01(after):
    print(after)
    print("---test01---")
