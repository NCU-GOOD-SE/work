# 领域模型 - 纯数据载体，无任何业务逻辑
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"角色：{self.name}，当前位置：{self.location}"


class World:
    def __init__(self, scenes):
        self.scenes = scenes  # 场景列表，例如 ["Forest", "Village"]


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"物品：{self.name} - {self.description}"


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name == item_name:
                return self.items.pop(i)
        return None

    def list_items(self):
        return [str(item) for item in self.items]