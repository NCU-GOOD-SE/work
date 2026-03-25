# 数据层 - 唯一访问全局状态的地方，封装所有数据操作
from domain_models import World

class GameStateRepository:
    def __init__(self):
        self._player = None  # 私有变量，外部禁止直接访问
        self._world = World(["Forest", "Village"])  # 初始化世界

    # 获取角色
    def get_player(self):
        return self._player

    # 保存/更新角色
    def save_player(self, player):
        self._player = player

    # 获取世界对象
    def get_world(self):
        return self._world

    # 添加新场景
    def add_scene(self, scene):
        if scene not in self._world.scenes:
            self._world.scenes.append(scene)
            return True, "场景添加成功"
        return False, "场景已存在"

    # 获取所有可用场景
    def get_all_scenes(self):
        return self._world.scenes