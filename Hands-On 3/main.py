import time
import numpy as np
import matplotlib.pyplot as plt

# Given f(n) function
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1
    return x

n_values = list(range(1, 1000)) 
times = [] 

# calculate time
for n in n_values:
    start_time = time.time() 
    f(n)  
    end_time = time.time()
    
    elapsed_time = end_time - start_time  
    times.append(elapsed_time)  

# cconvert n_values and times to numpy arrays for curve fitting
n_values_np = np.array(n_values)
times_np = np.array(times)

# fitting the quadratic curve (polynomial)
coefficients = np.polyfit(n_values_np, times_np, 2)
fitted_times = np.polyval(coefficients, n_values)

# Plot the times vs fitted curve
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, label="Actual Time")
plt.plot(n_values, fitted_times, label="Fitted Quadratic Curve", color='r')
plt.xlabel('n (Input Size)')
plt.ylabel('Time (Seconds)')
plt.title('Execution Time of f(n) vs Input Size n')
plt.legend()
plt.grid(True)
plt.show()

# check - polynomial equation
# print("Fitted polynomial coefficients (quadratic):", coefficients)

# Find Upper and Lower Bounds (Big-O, Big-Omega, Big-Theta)
upper_bound = coefficients[0] * n_values_np**2
lower_bound = coefficients[0] * n_values_np**2 * 0.8  # just considering an example for lower bound

# Plot upper and lower bounds
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, label="Actual Time")
plt.plot(n_values, fitted_times, label="Fitted Quadratic Curve", color='r')
plt.plot(n_values, upper_bound, label="Upper Bound", color='g')
plt.plot(n_values, lower_bound, label="Lower Bound", color='orange')
plt.xlabel('n (Input Size)')
plt.ylabel('Time (Seconds)')
plt.title('Upper and Lower Bounds for Execution Time of f(n)')
plt.legend()
plt.grid(True)
plt.show()

# Approximate n_0
n_0_index = np.where(times_np > fitted_times)[0][0]

plt.figure(figsize=(10, 6))
plt.plot(n_values, times, label="Actual Time")
plt.plot(n_values, fitted_times, label="Fitted Quadratic Curve", color='r')
plt.axvline(x=n_values[n_0_index], color='k', linestyle='--', label=f"n_0 ~ {n_values[n_0_index]}")
plt.xlabel('n (Input Size)')
plt.ylabel('Time (Seconds)')
plt.title('Approximation of n_0 (Where Actual Time Diverges)')
plt.legend()

plt.grid(True)
plt.show()

print(f"Approximate n_0: {n_values[n_0_index]}")
