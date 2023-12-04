import pytest

@pytest.fixture()
def first_entry():

    return "a"
@pytest.fixture()
def order(first_entry):
    return "b"


@pytest.fixture(autouse=True)
def append_first(order,first_entry):
    print("我被调用了")

def test_01(order,first_entry):
    pass

def test_02(order,first_entry):
    pass