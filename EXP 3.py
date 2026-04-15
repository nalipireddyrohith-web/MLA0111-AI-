from collections import deque

grid = [[0,0,0],
        [0,1,0],
        [0,0,0]]

rows, cols = 3,3
queue = deque([(0,0)])
visited = set([(0,0)])

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    r,c = queue.popleft()
    print((r,c), end=" ")

    for dr,dc in dirs:
        nr,nc = r+dr, c+dc
        if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
            visited.add((nr,nc))
            queue.append((nr,nc))
