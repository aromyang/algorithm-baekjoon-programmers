from collections import defaultdict

def solution(edges):
    out_edges = defaultdict(int)
    in_edges = defaultdict(int)

    for start_node, end_node in edges:
        out_edges[start_node] += 1
        in_edges[end_node] += 1

    bar_graphs = 0
    eight_graphs = 0
    start_node = None

    for node in set(out_edges.keys()).union(in_edges.keys()):
        out_count = out_edges[node]
        in_count = in_edges[node]

        if out_count == 0:
            bar_graphs += 1
        elif out_count == 2:
            if in_count > 0:
                eight_graphs += 1
            else:
                start_node = node
        elif out_count > 2:
            start_node = node

    donut_graphs = out_edges[start_node] - bar_graphs - eight_graphs

    return [start_node, donut_graphs, bar_graphs, eight_graphs]
