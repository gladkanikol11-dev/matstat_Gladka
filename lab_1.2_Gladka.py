import math
n = 5
p = 0.3
k = 2

prob = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
print(f"Ймовірність рівно {k} успіхів із {n}: {prob:.4f}")
