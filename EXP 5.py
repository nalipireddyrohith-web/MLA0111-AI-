grid = [[0,0,0],
        [0,1,0],
        [0,0,0]]

rows, cols = 3,3
visited = set()

def dfs(r,c):
    if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited:
        return

    visited.add((r,c))
    print((r,c), end=" ")

    dfs(r+1,c)
    dfs(r-1,c)
    dfs(r,c+1)
    dfs(r,c-1)

dfs(0,0)
