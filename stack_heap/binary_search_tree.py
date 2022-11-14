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
            current = self.head
            while True:
                if current.val < val:
                    if current.right is None:
                        current.right = Node(val)
                        break
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = Node(val)
                        break
                    else:
                        current = current.left

    def contains(self, val):
        current = self.head
        while current is not None:
            current_val = current.val
            if current_val == val:
                return True
            elif current_val > val:
                current = current.left
            else:
                current = current.right
        return False

    def remove(self, val):
        if self.head is not None:
            prev = self.head
            current = prev
            next_larger_val = 0
            while True:
                if current.val == val:
                    if current.left is None and current.right is None:
                        if prev is self.head:
                            self.head = None
                        else:
                            if current.val > prev.val:
                                prev.right = None
                            else:
                                prev.left = None
                        del current
                        return
                    elif current.left is None:
                        if current.val > prev.val:
                            prev.right = current.right
                        else:
                            prev.left = current.right
                        del current
                        return
                    elif current.right is None:
                        if current.val > prev.val:
                            prev.right = current.left
                        else:
                            prev.left = current.left
                        del current
                        return
                    else:
                        next_larger_node = current.right
                        while next_larger_node is not None:
                            next_larger_val = next_larger_node.val
                            next_larger_node = next_larger_node.left
                        self.remove(next_larger_val)
                        current.val = next_larger_val
                        return

                elif current.val > val:
                    if current.left is not None:
                        prev = current
                        current = current.left
                    else:
                        return
                else:
                    if current.right is not None:
                        prev = current
                        current = current.right
                    else:
                        return

    def pre_order_trav(self, node):
        if node is not None:
            print(node.val)
            self.pre_order_trav(node.left)
            self.pre_order_trav(node.right)

    def in_order_trav(self, node):
        if node is not None:
            self.in_order_trav(node.left)
            print(node.val)
            self.in_order_trav(node.right)

    def post_order_trav(self, node):
        if node is not None:
            self.post_order_trav(node.left)
            self.post_order_trav(node.right)
            print(node.val)


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
print('--------------------------')
bt.post_order_trav(bt.head)
print('--------------------------')
bt.pre_order_trav(bt.head)
print('remove 10')
bt.remove(10)
bt.pre_order_trav(bt.head)

#
# bt.contains(5)
# bt.contains(7)