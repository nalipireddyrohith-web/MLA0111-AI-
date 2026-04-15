def dfs(a, b, target, x, y, visited):
    if (a, b) in visited:
        return
    visited.add((a, b))

    print((a, b))

    if a == target or b == target:
        print("Goal reached")
        return

    # Fill
    dfs(x, b, target, x, y, visited)
    dfs(a, y, target, x, y, visited)

    # Empty
    dfs(0, b, target, x, y, visited)
    dfs(a, 0, target, x, y, visited)

    # Pour a -> b
    t = min(a, y-b)
    dfs(a-t, b+t, target, x, y, visited)

    # Pour b -> a
    t = min(b, x-a)
    dfs(a+t, b-t, target, x, y, visited)

dfs(0, 0, 2, 4, 3, set())
