def dfs(graph):
    visited = set()
    networks = 0
    for node in graph : 
        if dfs_rec(node, graph, visited) : networks += 1
    return networks
    
def dfs_rec(node, graph, visited):
    if node in visited : return 
    visited.add(node)
    for nd in graph[node] : dfs_rec(nd, graph, visited)
    return visited

def solution(n, computers):
    graph = {}
    for i, computer in enumerate(computers):
        graph[i] = []
        for i2, com in enumerate(computer) : 
            if com == 1 and i != i2 : graph[i].append(i2)
    return dfs(graph)
    