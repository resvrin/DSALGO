
class _Node:
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class BST1:
    def __init__(self):
        self.root = None

    def add_node(self, e):

        if self.root is None:
            self.root = _Node(e)
        elif e == self.root:
            return None
        elif e > self.root.element:
            new_node = self.root.right
            new_node = _Node(e)
        else:
            new_node = self.root.left
            new_node = _Node(e)

    def traverse_right(self):
        current = self.root
        while current.right:
                current = current.right
        return current




if __name__ == '__main__':
    tree = BST1()
    for i in range(5):
        tree.add_node(int(i))
    tree.traverse()








