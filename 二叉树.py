"""
先序遍历: 根节点->左子树->右子树
中序遍历: 左子树->根节点->右子树
后序遍历: 左子树->右子树->根节点
"""


class Node(object):
    """节点类"""
    def __init__(self, item):
        self.item = item
        self.lc = None
        self.rc = None


class BinaryTree(object):
    """二叉树"""
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        """广度优先添加节点"""
        if self.root is None:
            self.root = Node(item)
        else:
            queue = list()
            queue.append(self.root)
            while True:
                node = queue.pop(0)
                if not node.lc:
                    node.lc = Node(item)
                    break
                elif not node.rc:
                    node.rc = Node(item)
                    break
                else:
                    queue.append(node.lc)
                    queue.append(node.rc)

    def breath_search(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = list()
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.item, end=" ")
            if node.lc:
                queue.append(node.lc)
            if node.rc:
                queue.append(node.rc)

    def pre_order(self, root):
        """深度优先-先序遍历"""
        if root is None:
            return
        print(root.item, end=" ")
        self.pre_order(root.lc)
        self.pre_order(root.rc)

    def in_order(self, root):
        """深度优先-中序遍历"""
        if root is None:
            return
        self.pre_order(root.lc)
        print(root.item, end=" ")
        self.pre_order(root.rc)

    def post_order(self, root):
        """深度优先-后序遍历"""
        if root is None:
            return
        self.pre_order(root.lc)
        self.pre_order(root.rc)
        print(root.item, end=" ")


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.breath_search()
    print()

    bt.pre_order(bt.root)
    print()
    bt.in_order(bt.root)
    print()
    bt.post_order(bt.root)

