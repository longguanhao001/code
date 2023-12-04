import pytest
# 默认情况下用例的运行顺序是从上往下运行
# 设置了 运行顺序 用例 比没有设置先运行 错误的
# 设置优先级 设置了正数标记 > 没有标记 > 设置了复数的标记
# 相同的优先级情况 标记了运行顺序 数字小的先运行
# 没有标记的就是默认情况 从上往下运行

class Test_Order:

    @pytest.mark.run(order=-1)
    def test_01(self):
        print("-----test01--- ")

    @pytest.mark.run(order=-2)
    def test_02(self):
        print("-----test02--- ")

    def test_03(self):
        print("-----test03--- ")

    def test_04(self):
        print("-----test04--- ")

    @pytest.mark.run(order=2)
    def test_05(self):
        print("-----test05--- ")

    @pytest.mark.run(order=1)
    def test_06(self):
        print("-----test06--- ")