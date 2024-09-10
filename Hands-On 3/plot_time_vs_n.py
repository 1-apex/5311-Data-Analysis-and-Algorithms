import time
import matplotlib.pyplot as plt

# given function
def f(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
    return x

def measure_time(n):
    start_time = time.time()
    f(n)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    n_values = list(range(1, 1000))
    times = [measure_time(n) for n in n_values]
    
    # plot n vs time
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, label='Measured Time')
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title('Time vs n')
    plt.legend()
    plt.grid(True)
    plt.show()
