class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.head = None

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            cur = self.head
            while True:
                if cur.val < val:
                    if cur.right is None:
                        cur.right = Node(val)
                        break
                    else:
                        cur = cur.right
                else:
                    if cur.left is None:
                        cur.left = Node(val)
                        break
                    else:
                        cur = cur.left

    def contains(self, val):
        cur = self.head
        while cur is not None:
            cur_val = cur.val
            if cur_val == val:
                return True
            elif cur_val > val:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def remove(self, val):
        if self.head is not None:
            prev = self.head
            cur = prev
            while True:
                if cur.val == val:
                    if cur.left is None and cur.right is None:
                        if prev is self.head():
                            self.head = None
                        else:
                            if cur.val > prev.val:
                                prev.right = None
                            else:
                                prev.left = None
                        del cur
                    elif cur.left is None:
                        if cur.val > prev.val:
                            prev.right = cur.right
                        else:
                            prev.left = cur.right
                        del cur
                    elif cur.right is None:
                        if cur.val > prev.val:
                            prev.right = cur.left
                        else:
                            prev.left = cur.left
                        del cur
                    else:
                        next_larger_node = cur.right
                        while next_larger_node is not None:
                            next_larger_val = cur.right.val
                            next_larger_node = next_larger_node.left
                        self.remove(next_larger_val)
                        cur.val = next_larger_val

                elif cur.val > val:
                    if cur.left is not None:
                        prev = cur
                        cur = cur.left
                    else:
                        return
                else:
                    if cur.right is not None:
                        prev = cur
                        cur = cur.right
                    else:
                        return

    def in_order_trav(self, node):
        # just switch the order of print to have different types of traverse
        if node is not None:
            print(node.val)
            self.in_order_trav(node.left)
            self.in_order_trav(node.right)


bt = BinarySearchTree()
bt.add(10)
bt.add(5)
bt.add(15)
bt.add(1)
bt.add(6)
bt.add(12)
bt.add(14)
bt.add(17)
bt.in_order_trav(bt.head)
bt.remove(12)
bt.in_order_trav(bt.head)

#
# bt.contains(5)
# bt.contains(7)