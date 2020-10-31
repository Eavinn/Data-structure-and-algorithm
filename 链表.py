"""
链表，将元素存放在通过链接构造起来的一系列存储块中。
单向链表:链表中最简单的一种形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。
双向链表:每个节点有两个链接：一个指向前一个节点，当此节点为第一个节点时，指向空值；而另一个指向下一个节点，当此节点为最后一个节点时，指向空值
单向循环链表：单向链表中最后一个节点的next域不再为None，而是指向链表的头节点。
"""


class SingleNode(object):
    """单链表的节点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class DoubleNode(object):
    """双向链表节点"""
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class SingleLinkList(object):
    """单向链表"""
    def __init__(self):
        """__head属性不能继承，用_head方便继承"""
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        count = 0
        cur = self._head
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur is not None:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        """头部添加元素"""
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            cur = self._head
            while count < pos-1:
                cur = cur.next
                count += 1
            # 先将新节点node的next指向插入位置的节点
            node.next = cur.next
            # 将插入位置的前一个节点的next指向新节点
            cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


class DLinkList(SingleLinkList):
    """双向链表"""
    def add(self, item):
        """头部插入元素"""
        node = DoubleNode(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        """尾部插入元素"""
        node = DoubleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = DoubleNode(item)
            count = 0
            cur = self._head
            while count < pos-1:
                cur = cur.next
                count += 1
            # 将node的prev指向cur
            node.prev = cur
            # 将node的next指向cur的下一个节点
            node.next = cur.next
            # 将cur的下一个节点的prev指向node
            cur.next.prev = node
            # 将cur的next指向node
            cur.next = node

    def remove(self, item):
        """删除元素"""
        cur = self._head
        while cur is not None:
            if cur.item == item:
                # 先判断此结点是否是头节点
                if cur == self._head:
                    self._head = cur.next
                    # 如果存在下一个结点，则设置下一个结点
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


class SinCycLinkedlist(SingleLinkList):
    """单向循环链表"""
    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.item)
            cur = cur.next
        print(cur.item)

    def add(self, item):
        """头部添加节点"""
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 添加的节点指向_head
            node.next = self._head
            # 移到链表尾部，将尾部节点的next指向node
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            # _head指向添加node的
            self._head = node

    def append(self, item):
        """尾部添加节点"""
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self._head
        pre = None
        # 若删除的是头节点
        if cur.item == item:
            # 一个元素
            if cur.next == self._head:
                self._head = None
            # 多个元素
            else:
                while cur.next != self._head:
                    cur = cur.next
                cur.next = self._head.next
                self._head = self._head.next
        else:
            while cur.next != self._head:
                if cur.item == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            if cur.item == item:
                pre.next = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.item == item:
                return True
            cur = cur.next
        if cur.item == item:
            return True
        return False


if __name__ == '__main__':
    ll = SinCycLinkedlist()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:", ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(7))
    ll.remove(1)
    print("length:", ll.length())
    ll.travel()
