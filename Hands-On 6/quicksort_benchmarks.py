import sys
import time
import random
import matplotlib.pyplot as plt
# increase recursion limit 
sys.setrecursionlimit(10000000)

# Non random quicksort
def partition(arr, low, high):
    pivot = arr[low] 
    i = low + 1
    
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def benchmark_quicksort(arr):
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# Best case
def generate_best_case(n):
    return list(range(n))

# Worst case
def generate_worst_case(n):
    return list(range(n, 0, -1))

# Average case
def generate_average_case(n):
    return [random.randint(0, n) for _ in range(n)]

def run_benchmarks():
    sizes = [100, 200, 350, 500, 750, 1000, 2500, 5000, 7500, 10000]  
    best_case_times = []
    worst_case_times = []
    average_case_times = []

    # Benchmark tests
    for n in sizes:
        # Best case
        best_case_input = generate_best_case(n)
        best_case_times.append(benchmark_quicksort(best_case_input.copy()))

        # Worst case
        worst_case_input = generate_worst_case(n)
        worst_case_times.append(benchmark_quicksort(worst_case_input.copy()))

        # Average case
        average_case_input = generate_average_case(n)
        average_case_times.append(benchmark_quicksort(average_case_input.copy()))

    plt.plot(sizes, best_case_times, label="Best Case (Sorted Input)", marker="o")
    plt.plot(sizes, worst_case_times, label="Worst Case (Reverse Sorted Input)", marker="o")
    plt.plot(sizes, average_case_times, label="Average Case (Random Input)", marker="o")

    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort Performance for Non-Random Pivot')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_benchmarks()
