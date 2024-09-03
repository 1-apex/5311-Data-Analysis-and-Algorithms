import SelectionSort, InsertionSort, BubbleSort
import time
import random
import matplotlib.pyplot as plt

# get the time of each algorithms performance
def benchmark_sorting_algorithm(sort_function, sizes):
    times = []
    for size in sizes:
        # generating random integers for the array
        arr = [random.randint(-10000, 10000) for _ in range(size)]
        
        start_time = time.time()
        sort_function(arr)
        end_time = time.time()
        
        times.append(end_time - start_time)

    return times

# graphically representing the times of each algorithm
def plot_benchmark_results(sizes, selection_times, bubble_times, insertion_times):
    plt.figure(figsize=(10, 6))
    
    plt.plot(sizes, selection_times, label="Selection Sort")
    plt.plot(sizes, bubble_times, label="Bubble Sort")
    plt.plot(sizes, insertion_times, label="Insertion Sort")
    
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Benchmarking Sorting Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()


# input sizes to test the algorithms
sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]


# Running the benchmarks
selection_times = benchmark_sorting_algorithm(SelectionSort.selectionSort, sizes)
bubble_times = benchmark_sorting_algorithm(BubbleSort.bubbleSort, sizes)
insertion_times = benchmark_sorting_algorithm(InsertionSort.insertionSort, sizes)


# Plot the results
plot_benchmark_results(sizes, selection_times, bubble_times, insertion_times)
