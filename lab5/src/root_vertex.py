def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        graph = [[] for _ in range(n)]
        for line in file:
            u, v = map(int, line.strip().split())
            graph[u].append(v)
    return graph

def dfs(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.extend(graph[node])

def is_root_vertex(graph, start):
    visited = [False] * len(graph)
    dfs(graph, start, visited)
    return all(visited)

def find_root_vertex(graph):
    for i in range(len(graph)):
        if is_root_vertex(graph, i):
            return i
    return -1

def main():
    graph = read_graph_from_file("lab5/input.txt")
    root = find_root_vertex(graph)
    with open("lab5/output.txt", "w") as file:
        file.write(str(root))

if __name__ == "__main__":
    main()
