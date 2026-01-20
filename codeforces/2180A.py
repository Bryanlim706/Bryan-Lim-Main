import math

amt_of_samples = int(input())
for _ in range(amt_of_samples):
    l, a, b = map(int, input().split())
    b %= l

    g = math.gcd(l, b)
    print(a + (((l - 1 - a) // g) * g))


