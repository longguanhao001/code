
# 模块级别，先执行
def setup_module():
    print("---setup_module---")

# 模块级别，最后执行
def teardown_module():
    print("---teardown_module---")

# 函数级别的，不会夹类里面的方法
def setup_function():
    print("---setup_function---")

def tear_function():
    print("---tear_function---")





def test_d():
    print("----test_d---")

def test_e():
    print("----test_e---")


class TestSecond:
    # 类级别的夹具
    def setup_class(self):
        print("----setup_class---")

    def teardown_class(self):
        print("----teardown_class---")

    # 方法级别的
    def setup_method(self):
        print("----setup_method---")

    def teardown_method(self):
        print("----teardown_method---")




    def test_01(self):
        print("----test_01---")


    def test_02(self):
        print("----test_02---")

    def test_03(self):
        print("----test_03---")