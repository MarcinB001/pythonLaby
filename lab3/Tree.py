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

    @property
    def min_value(self):
        def find_min(node):
            min_val = node.value
            for child in node.children:
                child_min = find_min(child['node'])
                min_val = min(min_val, child_min)

            return min_val

        return find_min(self)


if __name__ == '__main__':
    tree = Node(5)
    node1 = Node(4)
    node2 = Node(1)
    node3 = Node(2)

    tree.add_child(node1, 1)
    tree.add_child(node2, 2)
    node2.add_child(node3, 3)

    print(tree)

    print(f'Najmniejsza wartosc:  {tree.min_value}')

