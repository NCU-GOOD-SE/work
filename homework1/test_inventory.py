import unittest
from domain_models import Item, Inventory
from services import InventoryService
from repository import GameStateRepository

class TestInventory(unittest.TestCase):
    def test_create_inventory(self):
        """测试创建背包"""
        inv = Inventory()
        self.assertEqual(len(inv.items), 0)

    def test_add_item(self):
        """测试添加物品"""
        inv = Inventory()
        item = Item("剑", "一把锋利的剑")
        inv.add_item(item)
        self.assertEqual(len(inv.items), 1)

    def test_remove_item(self):
        """测试移除物品"""
        inv = Inventory()
        inv.add_item(Item("剑", "一把锋利的剑"))
        removed = inv.remove_item("剑")
        self.assertIsNotNone(removed)
        self.assertEqual(len(inv.items), 0)

    def test_remove_nonexistent_item(self):
        """测试移除不存在的物品"""
        inv = Inventory()
        removed = inv.remove_item("不存在的物品")
        self.assertIsNone(removed)

    def test_list_items(self):
        """测试列出物品"""
        inv = Inventory()
        inv.add_item(Item("剑", "一把锋利的剑"))
        inv.add_item(Item("盾", "一个坚固的盾"))
        items = inv.list_items()
        self.assertEqual(len(items), 2)

    def test_inventory_service_pickup(self):
        """测试拾取物品"""
        repo = GameStateRepository()
        service = InventoryService(repo)
        
        success, msg = service.pick_up("钥匙")
        self.assertTrue(success)
        self.assertIn("钥匙", msg)

    def test_inventory_service_show(self):
        """测试查看背包"""
        repo = GameStateRepository()
        service = InventoryService(repo)
        
        service.pick_up("钥匙")
        service.pick_up("金币")
        
        success, msg = service.show_inventory()
        self.assertTrue(success)
        self.assertIn("钥匙", msg)
        self.assertIn("金币", msg)

    def test_inventory_service_drop(self):
        """测试丢弃物品"""
        repo = GameStateRepository()
        service = InventoryService(repo)
        
        service.pick_up("钥匙")
        success, msg = service.drop_item("钥匙")
        self.assertTrue(success)
        
        # 再次拾取应该失败
        success, msg = service.drop_item("钥匙")
        self.assertFalse(success)

    def test_pickup_empty_name(self):
        """测试拾取空名称"""
        repo = GameStateRepository()
        service = InventoryService(repo)
        
        success, msg = service.pick_up("")
        self.assertFalse(success)

if __name__ == '__main__':
    unittest.main()
