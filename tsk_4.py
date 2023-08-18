tree_in = {
    1: [2, 7],
    2: [3, 4],
    3: [None, None],
    4: [5, None],
    5: [None, None],
    6: [None, None],
    7: [None, 9],
    8: [None, None],
    9: [None, None]
}


def show_tree(node, tree=tree_in):
    if node is None:
        return
    print(node)

    show_tree(tree[node][0])
    show_tree(tree[node][1])


show_tree(1)



    