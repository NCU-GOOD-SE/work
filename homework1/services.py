# 业务逻辑层 - 纯逻辑处理，不处理输入输出
from domain_models import Player, Item

class CharacterService:
    def __init__(self, repo):
        self.repo = repo  # 依赖注入数据层

    # 创建角色
    def create(self, name):
        if self.repo.get_player():
            return False, "角色已存在，无法重复创建"
        if not name or name.strip() == "":
            return False, "角色名字不能为空"
        # 创建角色并默认出生在 Forest
        new_player = Player(name.strip(), "Forest")
        self.repo.save_player(new_player)
        return True, f"角色【{name}】创建成功！"

    # 查看角色状态
    def status(self):
        player = self.repo.get_player()
        if not player:
            return False, "请先创建角色"
        return True, str(player)


class MovementService:
    def __init__(self, repo):
        self.repo = repo

    # 移动角色到目标场景
    def move(self, target):
        player = self.repo.get_player()
        if not player:
            return False, "请先创建角色"
        # 校验场景是否存在
        if target not in self.repo.get_all_scenes():
            return False, f"场景【{target}】不存在，无法移动"
        # 执行移动
        player.location = target
        return True, f"已移动至：{target}"


class SceneService:
    def __init__(self, repo):
        self.repo = repo

    # 查看所有场景
    def list_scenes(self):
        scenes = self.repo.get_all_scenes()
        return True, f"可用场景：{', '.join(scenes)}"

    # 添加场景
    def add_scene(self, scene):
        return self.repo.add_scene(scene)


class InventoryService:
    def __init__(self, repo):
        self.repo = repo

    def pick_up(self, item_name, description=""):
        if not item_name:
            return False, "物品名称不能为空"
        new_item = Item(item_name, description or "一件普通物品")
        self.repo.add_item_to_inventory(new_item)
        return True, f"获得了：{item_name}"

    def drop_item(self, item_name):
        item = self.repo.remove_item_from_inventory(item_name)
        if item:
            return True, f"丢弃了：{item_name}"
        return False, f"背包里没有：{item_name}"

    def show_inventory(self):
        items = self.repo.get_inventory().list_items()
        if not items:
            return True, "背包是空的"
        return True, "背包物品：\n" + "\n".join(items)