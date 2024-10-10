import time

# Recursive Fibonacci
def fibo_rec(i):
    if i == 0 :
        return 0 
    if i == 1 :
        return 1
    else :
        return fibo_rec(i - 1)+fibo_rec(i - 2)
    
# Iterative Fibonacci   
def fibo_it(i):
    if i == 0 :
        return 0
    else : 
        x,y = 0,1
        for j in range(2, i + 1):
            temp = x + y
            x = y
            y = temp
        return y

# Smart Recursive Fibonacci with an auxiliary function   
def fibo_smart_rec_aux(i):
    if i == 0 :
        return 0, 0
    if i == 1 :
        return 1, 0
    f_i_1, f_i_2 = fibo_smart_rec_aux(i - 1)
    return f_i_1 + f_i_2, f_i_1

def fibo_smart_rec(i):
    x, y = fibo_smart_rec_aux(i - 1)
    return x + y

n = int(input("enter n : "))
t_0 = time.time()
fibo_it(n)
t_1 = time.time()
elapsed_time_it = (t_1 - t_0) * 1000 
print(f">> runing time on rec : {elapsed_time_it:.4f} ms")
t_0 = time.time()
fibo_rec(n)
t_1 = time.time()
elapsed_time_it = (t_1 - t_0) * 1000 
print(f">> runing time on it : {elapsed_time_it:.4f} ms")
t_0 = time.time()
fibo_smart_rec(n)
t_1 = time.time()
elapsed_time_it = (t_1 - t_0) * 1000 
print(f">> runing time on smart : {elapsed_time_it:.4f} ms")
    
