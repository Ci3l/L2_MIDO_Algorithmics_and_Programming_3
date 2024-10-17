import math
import random
import time

def racine_carree(A:int) :
    epsilon = 1e-30
    X = random.randint(0,A)
    while epsilon<abs(X-math.sqrt(A)) :
        X  = (1/2)*(X+A/X)
    return X


i=9
t_0 = time.time()
print(racine_carree(i))
t_1 = time.time()
elapsed_time = t_1-t_0
print(f'elapsed_time : {elapsed_time:.9f}')
t_0 = time.time()
print(math.sqrt(i))
t_1 = time.time()
elapsed_time = t_1-t_0
print(f'elapsed_time : {elapsed_time:.9f}')