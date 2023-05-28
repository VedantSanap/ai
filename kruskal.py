def kruskal(vertices, edges):
    parent = list(range(vertices))
    rank = [0] * vertices
    result = []
    edges.sort(key=lambda x: x[2])

    def find(i):
        return i if parent[i] == i else find(parent[i])

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            rank[root_y] += 1

    for u, v, w in edges:
        if len(result) < vertices - 1 and find(u) != find(v):
            result.append([u, v, w])
            union(u, v)

    return result

num_vertices = 5
graph_edges = [[0, 1, 2], [0, 2, 1], [1, 3, 4], [1, 2, 3], [2, 4, 5], [3, 4, 6]]

mst = kruskal(num_vertices, graph_edges)
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} : {weight}")