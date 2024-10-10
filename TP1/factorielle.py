def factorielle_iterative(i) :
    r = 1
    if i > 2 :
        for j in range(2, i + 1):
            r = r * j
        i = r
    return i

def factorielle_recursive(i):
    if i > 1 :
        return factorielle_recursive(i - 1) * i

# Testing the functions
print(factorielle_iterative(3))
print(factorielle_recursive(5))

