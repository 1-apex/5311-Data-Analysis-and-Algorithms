import time
import matplotlib.pyplot as plt
import numpy as np

# given function
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1
    return x

def measure_time(n):
    start_time = time.time()
    f(n)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    n_values = list(range(1, 1000))
    times = [measure_time(n) for n in n_values]

    # Convert n_values and times to numpy arrays for curve fitting
    n_values_np = np.array(n_values)
    times_np = np.array(times)

    # Fit a quadratic curve (degree 2 polynomial)
    coefficients = np.polyfit(n_values_np, times_np, 2)
    polynomial = np.poly1d(coefficients)

    # Generate fitted curve values
    fitted_times = polynomial(n_values_np)

    # Plotting the actual times vs fitted curve
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, label="Actual Time")
    plt.plot(n_values, fitted_times, label="Fitted Quadratic Curve", color='r')

    # Add labels and title
    plt.xlabel('n (Input Size)')
    plt.ylabel('Time (Seconds)')
    plt.title('Execution Time of f(n) vs Input Size n')
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()