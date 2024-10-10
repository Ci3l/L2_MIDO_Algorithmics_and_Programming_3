import math

# Iterative Power Function
def puissance_it(x, n):
    r = 1
    for i in range(n):
        r = r * x
    return r

# Recursive Power Function
def puissance_rec(x, n):
    if n > 0 :
        return puissance_rec(x, n - 1) * x
    return 1

# Optimized Recursive Power Function
def puissance_smart_rec(x,n):
    if n > 0 :
        if n % 2 == 0 :
            return puissance_smart_rec(x,n // 2) ** 2
        else :
            return x * puissance_smart_rec(x,math.floor(n / 2))
    return 1