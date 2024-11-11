from collections import defaultdict

def dfs(graph, vertex, visited):
    stack = [vertex]
    count_vertices = 0
    count_edges = 0
    
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            count_vertices += 1
            
            for neighbor in graph[v]:
                count_edges += 1
                if not visited[neighbor]:
                    stack.append(neighbor)
    
    return count_vertices, count_edges // 2

def check_connected_components(N, M, edges):
    # グラフの初期化
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    
    for vertex in range(1, N + 1):
        if not visited[vertex]:
            count_vertices, count_edges = dfs(graph, vertex, visited)
            if count_vertices != count_edges:
                return "No"
    
    return "Yes"

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = check_connected_components(n, m, edges)
print(result)
