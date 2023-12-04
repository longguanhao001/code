import sys

import pytest
def test_a():
    print("__testa__")
def test_b():
    print("__testb__")

# if __name__ == '__main__':
#     pytest.main(["-vs"])
#     pytest.main(["-vs","me"]) 指定运行me标记的用例


def test_01():
    print("__test01__")
    print(sys.version)
    print(sys.version[:3])

# 使用装饰器跳过执行W
@pytest.mark.skip(reason = "不想执行")
def test_02():
    print("__test02__")

# pytest.mark.fail(condition,reason=None,raises=None)
@pytest.mark.skipif(float(sys.version[:3]) >= 3.6,reason="python版本大于3.6就跳过不执行")
def test_03():
    print("__test03__")

# 标记失败，预期会出现的结果
@pytest.mark.xfail(raises = ZeroDivisionError)
def test_04():
    print("__test04__")
    1/0

def test_05():
    print("__test05__")

@pytest.mark.me
def test_06():
    print("__test06__")

@pytest.mark.you
def test_07():
    print("__test07__")


