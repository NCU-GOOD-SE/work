# 表现层 - 仅负责输入输出与命令路由，无业务逻辑
from repository import GameStateRepository
from services import CharacterService, MovementService, SceneService, InventoryService

def parse_input(user_input):
    """
    解析用户输入
    例如输入：create Tom  → 返回 ("create", "Tom")
         输入：move Village → 返回 ("move", "Village")
         输入：status      → 返回 ("status", "")
    """
    parts = user_input.strip().split(maxsplit=1)
    if len(parts) == 0:
        return "", ""
    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""
    return cmd, arg

def main():
    print("=== 文字冒险游戏 ===")
    print("命令：create [名字] | move [场景] | status | list | add [场景] | inventory | pickup [物品] | drop [物品] | quit\n")

    # 初始化依赖
    repo = GameStateRepository()
    char_service = CharacterService(repo)
    move_service = MovementService(repo)
    scene_service = SceneService(repo)
    inv_service = InventoryService(repo)  # 新增背包服务

    # 主循环
    while True:
        try:
            user_input = input("> ")
            cmd, arg = parse_input(user_input)

            if cmd == "quit":
                print("游戏结束")
                break

            elif cmd == "create":
                success, msg = char_service.create(arg)

            elif cmd == "status":
                success, msg = char_service.status()

            elif cmd == "move":
                success, msg = move_service.move(arg)

            elif cmd == "list":
                success, msg = scene_service.list_scenes()

            elif cmd == "add":
                success, msg = scene_service.add_scene(arg)

            # ===== 新增背包系统命令 =====
            elif cmd == "inventory":
                success, msg = inv_service.show_inventory()

            elif cmd == "pickup":
                success, msg = inv_service.pick_up(arg)

            elif cmd == "drop":
                success, msg = inv_service.drop_item(arg)
            # ===== 背包系统命令结束 =====

            else:
                msg = "未知命令，请重试"

            print(msg)
            print("-" * 30)

        except KeyboardInterrupt:
            print("\n游戏退出")
            break

if __name__ == "__main__":
    main()