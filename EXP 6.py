def dfs_path(graph, start, goal, path=[]):
    path = path + [start]

    if start == goal:
        return path

    for n in graph[start]:
        if n not in path:
            newpath = dfs_path(graph, n, goal, path)
            if newpath:
                return newpath

graph = {'A':['B','C'], 'B':['D'], 'C':['E'], 'D':[], 'E':[]}
print(dfs_path(graph,'A','E'))
