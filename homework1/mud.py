#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
极简控制台MUD游戏（MVP版）
Sprint 1 核心代码
支持：create / add / move / status / help / quit / 错误处理
"""

# 全局游戏状态存储
game_state = {
    "player": None,
    "scenes": ["Forest", "Village"],  # 初始场景
    "valid_commands": ["create", "add", "move", "status", "help", "quit"]
}

def print_separator():
    print("-" * 40)

def validate_location(location):
    return location in game_state["scenes"]

# ----------------------
# 1. 创建角色
# ----------------------
def handle_create(name):
    if not name:
        print("❌ 角色名不能为空！")
        return
    if game_state["player"]:
        print(f"⚠️  你已创建角色：{game_state['player']['name']}")
        return

    game_state["player"] = {
        "name": name,
        "location": "Forest"
    }
    print(f"✅ 角色创建成功！欢迎你，{name}！")
    print("💡 输入 'help' 查看可用指令")

# ----------------------
# 2. 添加场景（新增功能）
# ----------------------
def handle_add(scene):
    if not game_state["player"]:
        print("❌ 请先创建角色！")
        return

    if scene in game_state["scenes"]:
        print(f"⚠️  场景 {scene} 已存在！")
        return

    game_state["scenes"].append(scene)
    print(f"✅ 成功添加场景：{scene}")

# ----------------------
# 3. 移动场景
# ----------------------
def handle_move(target_location):
    if not game_state["player"]:
        print("❌ 请先创建角色！")
        return

    if not validate_location(target_location):
        print(f"❌ 无效场景！当前支持：{', '.join(game_state['scenes'])}")
        return

    game_state["player"]["location"] = target_location
    print(f"✅ 移动成功！你现在在：{target_location}")

# ----------------------
# 4. 查看状态
# ----------------------
def handle_status():
    if not game_state["player"]:
        print("❌ 请先创建角色！")
        return
    print("📋 角色状态：")
    print(f"   姓名：{game_state['player']['name']}")
    print(f"   当前位置：{game_state['player']['location']}")

# ----------------------
# 5. 帮助
# ----------------------
def handle_help():
    print("📖 可用指令：")
    print("   create <名字>   - 创建角色")
    print("   add <Forest/Marine> - 添加场景")
    print("   move <场景>     - 移动到场景")
    print("   status          - 查看状态")
    print("   help            - 查看帮助")
    print("   quit            - 退出游戏")

# ----------------------
# 主循环
# ----------------------
def main_game_loop():
    print("🎉 欢迎来到 MUD 游戏 MVP！")
    print_separator()
    handle_help()
    print_separator()

    while True:
        user_input = input("\n请输入指令 > ").strip()
        if not user_input:
            continue

        command_parts = user_input.split()
        main_command = command_parts[0].lower()

        if main_command == "create":
            if len(command_parts) < 2:
                print("❌ 用法：create <名字>")
            else:
                handle_create(command_parts[1])

        elif main_command == "add":
            if len(command_parts) < 2:
                print("❌ 用法：add <Forest/Marine>")
            else:
                handle_add(command_parts[1])

        elif main_command == "move":
            if len(command_parts) < 2:
                print("❌ 用法：move <场景>")
            else:
                handle_move(command_parts[1])

        elif main_command == "status":
            handle_status()

        elif main_command == "help":
            handle_help()

        elif main_command == "quit":
            print("👋 游戏结束！")
            break

        else:
            print(f"❌ 无效指令：{main_command}")
            print("💡 输入 help 查看用法")

if __name__ == "__main__":
    try:
        main_game_loop()
    except KeyboardInterrupt:
        print("\n👋 游戏已退出")
    except Exception as e:
        print(f"\n❌ 错误：{e}")