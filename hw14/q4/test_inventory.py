import pytest
from inventory import Inventory

invtry = Inventory()
i = 0


# it should be a class named testInventory obj should be in feacsture , test ha mostaghel bashan
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
def test_add_item(name, quantity):  # mohtava test konam
    global i
    i += 1
    invtry.add_item(name, quantity)
    assert len(invtry.items) == i


def test_remove_item():
    invtry.remove_item("maye_dast", 6)
    assert invtry.items.get("maye_dast") == 24

    with pytest.raises(KeyError):
        invtry.remove_item("egg", 3)
    with pytest.raises(ValueError):
        invtry.remove_item("maye_dast", 63)
        # print("quantity is less than 63")


# def test_remove_item():
#     with pytest.raises(KeyError):
#         invtry.remove_item("egg", 3)
#         print("egg does not exist..")


# def test_remove_item():
#     with pytest.raises(ValueError):
#         invtry.remove_item("maye_dast", 63)
#         print("quantity is less than 63")


def test_get_item_quantity():
    assert invtry.get_item_quantity("roghan") == 20
    assert invtry.get_item_quantity("kolah") == 2


# def test_get_item_quantity_2():
#     assert invtry.get_item_quantity("kolah") == 0


def test_get_total_items():
    assert invtry.get_total_items() == (165 - 6)
