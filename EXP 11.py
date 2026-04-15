import math

def can_measure(x, y, z):
    if z > max(x, y):
        return False
    return z % math.gcd(x, y) == 0

print(can_measure(4, 3, 2))  # True
