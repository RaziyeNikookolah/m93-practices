class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, quantity: int):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity

    def remove_item(self, name, quantity):
        if name not in self.items:
            raise KeyError("Item not found")
        if quantity > self.items[name]:
            raise ValueError("Insufficient quantity")
        self.items[name] -= quantity
        if self.items[name] == 0:
            del self.items[name]

    def get_item_quantity(self, name):
        return self.items.get(name, 0)

    def get_total_items(self):
        return sum(self.items.values())
