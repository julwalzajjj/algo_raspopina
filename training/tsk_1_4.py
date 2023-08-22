# Вам дан корень двоичного дерева. Верните среднее значение узлов на каждом уровне в виде 
# массива. Ответы, отличающиеся от фактического не более чем на 10^-5, будут приняты.

import collections

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mid_search(root):
    q = collections.deque()
    q = [root]
    while q:
        len_level = len(q)
        tmp = 0
        for _ in range(len_level):
            node = q.pop(0)
            if node:
                tmp += node.value
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        print(tmp/len_level)

tree = Tree(3)
tree.left = Tree(9)
tree.right = Tree(20)
tree.left.left = Tree(15)
tree.left.right = Tree(7)

mid_search(tree)

