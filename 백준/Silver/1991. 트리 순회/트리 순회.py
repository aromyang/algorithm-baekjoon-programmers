n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)


def pre_order(root):
    if root == '.':
        return
    print(root, end='')
    pre_order(tree.get(root)[0])
    pre_order(tree.get(root)[1])


def in_order(root):
    if root == '.':
        return
    in_order(tree.get(root)[0])
    print(root, end='')
    in_order(tree.get(root)[1])


def post_order(root):
    if root == '.':
        return
    post_order(tree.get(root)[0])
    post_order(tree.get(root)[1])
    print(root, end='')


pre_order('A')
print()
in_order('A')
print()
post_order('A')
