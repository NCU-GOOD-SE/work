#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
极简控制台 MUD 游戏（MVP 版）
Sprint 1 核心代码
负责：PO 陈以凡 - 框架搭建、help、quit
"""

# 全局游戏状态存储
game_state = {
    "player": None,
    "scenes": ["Forest", "Village"],
    "valid_commands": ["create", "add", "move", "status", "help", "quit"]
}

def print_separator():
    print("-" * 40)

# ----------------------
# 帮助指令
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
# 主循环框架
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
            pass

        elif main_command == "add":
            pass

        elif main_command == "move":
            pass

        elif main_command == "status":
            pass

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
