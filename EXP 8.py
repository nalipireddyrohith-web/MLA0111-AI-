from collections import deque

def water_jug(x, y, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        print((a, b))

        if a == target or b == target:
            print("Goal reached")
            return

        # Fill
        queue.append((x, b))
        queue.append((a, y))

        # Empty
        queue.append((0, b))
        queue.append((a, 0))

        # Pour a -> b
        t = min(a, y-b)
        queue.append((a-t, b+t))

        # Pour b -> a
        t = min(b, x-a)
        queue.append((a+t, b-t))

water_jug(4, 3, 2)
