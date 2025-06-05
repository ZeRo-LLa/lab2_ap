def read_edges_from_csv(filename):
    edges = []

    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue
            u, v, w = parts[0].strip(), parts[1].strip(), int(parts[2])
            edges.append((w, u, v))

    weight, mst = min_distanse(edges)
    if weight == -1:
        print(weight)
    else:
        print("Minimum Distance:", weight)
        print("MST edges:")
        for edge in mst:
            print(edge)


def min_distanse(edges):
    if not edges:
        return -1, []

    parent = {}
    rank = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
        return True

    nodes = set()
    for _, u, v in edges:
        nodes.add(u)
        nodes.add(v)
    for node in nodes:
        parent[node] = node
        rank[node] = 0

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]: 
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result


    edges = merge_sort(edges)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if union(u, v):
            mst.append((weight, u, v))
            total_weight += weight
            if len(mst) == len(nodes) - 1:
                break

    if len(mst) != len(nodes) - 1:
        return -1, []

    return total_weight, mst


print(read_edges_from_csv("lab2_ap/lab8/src/communication_wells.csv"))
