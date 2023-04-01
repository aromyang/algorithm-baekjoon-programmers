import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


class Tree:
    def __init__(self, root):
        self.tree = {root: []}

    def append_node(self, parent, child):
        if parent not in self.tree:
            self.tree[parent] = []
        if child not in self.tree:
            self.tree[child] = []
        self.tree[parent].append(child)
        self.tree[child].append(parent)

    def get_nodes(self, root):
        return self.tree[root]

    def dfs(self, cur_node, root_node, ans):
        ans[cur_node] = root_node
        for node in self.get_nodes(cur_node):
            if node != root_node:
                self.dfs(node, cur_node, ans)


n = int(input())
tree = Tree(1)

for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    tree.append_node(node1, node2)

ans = [0] * (n + 1)
tree.dfs(1, 0, ans)

for i in range(2, n + 1):
    print(ans[i])
