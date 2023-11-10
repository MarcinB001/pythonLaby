import unittest
from zad7 import Node


class TestNode(unittest.TestCase):
    def setUp(self):
        self.tree = Node("Root")
        self.node1 = Node("Node 1")
        self.node2 = Node("Node 2")
        self.node3 = Node("Node 3")

    def test_add_child(self):
        self.tree.add_child(self.node1, "Edge R-1")
        self.node1.add_child(self.node2, "Edge 1-2")
        self.node1.add_child(self.node3, "Edge 1-3")

        self.assertEqual(len(self.tree.children), 1)
        self.assertEqual(self.tree.children[0]["node"], self.node1)
        self.assertEqual(self.tree.children[0]["edge_value"], "Edge R-1")

        self.assertEqual(len(self.node1.children), 2)
        self.assertEqual(self.node1.children[0]["node"], self.node2)
        self.assertEqual(self.node1.children[0]["edge_value"], "Edge 1-2")
        self.assertEqual(self.node1.children[1]["node"], self.node3)
        self.assertEqual(self.node1.children[1]["edge_value"], "Edge 1-3")


unittest.main()
