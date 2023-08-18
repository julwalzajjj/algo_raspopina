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

def show_level(node, tree=tree_in):
    if node is None:
        return
    print(node)

    show_level(tree[node][0])
    show_level(tree[node][1])


# def show_tree_right(node, time=None, tree=tree_in):
#     if node is None:
#         return 
#     if time is None:
#         print(node)

#     show_tree_right(tree[node][1])

# def show_tree_left(node, tree=tree_in):
#     if node is None:
#         return 
#     print(node)

#     show_tree_left(tree[node][0])

# def show_tree(key):
#     show_tree_left(key)
#     show_tree_right(key, time=1)

show_level(1)