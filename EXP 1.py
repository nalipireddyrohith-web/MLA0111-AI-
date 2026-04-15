graph = {'A':['B','C'], 'B':['D'], 'C':['E'], 'D':[], 'E':[]}

visited = []
queue = ['A']

while queue:
    node = queue.pop(0)
    if node not in visited:
        visited.append(node)
        queue.extend(graph[node])

print("BFS:", visited)
