graph = {'A':['B','C'], 'B':['D'], 'C':['E'], 'D':[], 'E':[]}

visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(n)

dfs('A')
print("DFS:", visited)
