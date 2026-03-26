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