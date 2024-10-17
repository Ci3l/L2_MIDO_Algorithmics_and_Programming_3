import matplotlib.pyplot as plt
import random

def feigenbaum(mu: float, x_0: float, n: int):
    x = x_0
    sequence = []
    
    for i in range(n):
        x = 1 - mu * x ** 2
        sequence.append(x)
    
    return sequence

x_0 = 0.5  
n = 50     

mu_values = [   random.uniform(0.0,0.75),
                random.uniform(0.75,1.25),
                random.uniform(1.25,1.368),
                random.uniform(1.368,1.401),
                random.uniform(1.401,2)
            ]
colors = ['b', 'g', 'r', 'c', 'm']  
labels = [f'$\mu$ = {mu}' for mu in mu_values]  

# Plot each sequence with a different color and label
plt.figure(figsize=(10, 6))

for mu, color, label in zip(mu_values, colors, labels):
    sequence = feigenbaum(mu, x_0, n)
    indices = list(range(1, len(sequence) + 1))  # Generate x-axis values for plotting
    plt.plot(indices, sequence, marker='o', linestyle='-', color=color, label=label)

# Label the plot
plt.xlabel('Iteration (n)')
plt.ylabel('Value of x')
plt.title(f'Feigenbaum Sequences for Different Mu Values (x_0 = {x_0})')
plt.legend()
plt.grid(True)
plt.show()
