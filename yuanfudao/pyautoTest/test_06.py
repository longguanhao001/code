import pytest

@pytest.fixture()
def first_entry():
    return "a"

@pytest.fixture()
def order(first_entry):
    return[first_entry]


def test_01(order):
    print("---test01---")

    order.append("b")

    assert order == ["a", "b"]

@pytest.mark.usefixtures("order")
def test_03(order):
    print("---test03---")
    print(order)
