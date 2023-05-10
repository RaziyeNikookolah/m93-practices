import pytest
from inventory import Inventory

invtry = Inventory()
i = 0


@pytest.mark.parametrize(
    "name,quantity",
    [
        ("maye_dast", 30),
        ("ab_madani", 60),
        ("roghan", 20),
        ("shampoo", 10),
        ("sabun", 15),
        ("badanshoo", 20),
        ("dastkesh", 10),
    ],
)
def test_add_item(name, quantity):
    global i
    i += 1
    invtry.add_item(name, quantity)
    assert len(invtry.items) == i


def test_remove_item_1():
    invtry.remove_item("maye_dast", 6)
    assert invtry.items.get("maye_dast") == 24


def test_remove_item_2():
    with pytest.raises(KeyError):
        invtry.remove_item("egg", 3)
        print("egg does not exist..")


def test_remove_item_3():
    with pytest.raises(ValueError):
        invtry.remove_item("maye_dast", 63)
        print("quantity is less than 63")


def test_get_item_quantity_1():
    assert invtry.get_item_quantity("roghan") == 20


def test_get_item_quantity_2():
    assert invtry.get_item_quantity("kolah") == 0


def test_get_total_items():
    assert invtry.get_total_items() == (165 - 6)
