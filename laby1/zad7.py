class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, child, edge_value=None):
        self.children.append({"node": child, "edge_value": edge_value})

    def __str__(self, level=0):
        tree = "\t" * level + f"Node({self.value})\n"
        for child in self.children:
            tree += "\t" * (level + 1) + f"Edge({child['edge_value']})"
            tree += child["node"].__str__(level + 2)
        return tree


tree = Node("Root")
node1 = Node("Node 1")
node2 = Node("Node 2")
node3 = Node("Node 3")

tree.add_child(node1, "Edge R-1")
tree.add_child(node2, "Edge R-2")
node2.add_child(node3, "Edge 2-3")

print(tree)
