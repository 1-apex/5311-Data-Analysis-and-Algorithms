import random

# Non Random Quicksort
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

# Random Pivor Quicksort 
def partition_random(arr, low, high):
    rand_pivot = random.randint(low, high) 
    arr[low], arr[rand_pivot] = arr[rand_pivot], arr[low]
    return partition(arr, low, high)

def quicksort_random(arr, low, high):
    if low < high:
        pivot_index = partition_random(arr, low, high)
        quicksort_random(arr, low, pivot_index - 1)  
        quicksort_random(arr, pivot_index + 1, high) 


def test_quick_sort():
    test_cases = {
        "Case 1 - Already Sorted": [1, 2, 3, 4, 5, 6],
        "Case 2 - Reverse Sorted": [6, 5, 4, 3, 2, 1],
        "Case 3 - All Identical": [5, 5, 5, 5, 5, 5],
        "Case 4 - Random Order": [3, 1, 4, 2, 6, 5],
        "Case 5 - Large Range": [1000, 200, 3000, 600, 150, 50],
        "Case 6 - Empty Array": [],
        "Case 7 - Single Element": [1],
        "Case 8 - Two Elements (Sorted)": [1, 2],
        "Case 9 - Two Elements (Unsorted)": [2, 1]
    }

    for case_name, arr in test_cases.items():
        # Non-Random Pivot quicksort
        arr_copy = arr.copy()  
        print(f"{case_name} (Non-Random Pivot):")\
            
        quicksort(arr_copy, 0, len(arr_copy) - 1)
        
        print("Sorted:", arr_copy)
        
        # Random Pivot Quicksort
        arr_copy = arr.copy() 
        print(f"{case_name} (Random Pivot):")
        
        quicksort_random(arr_copy, 0, len(arr_copy) - 1)
        
        print("Sorted:", arr_copy)
        print("---------")

if __name__ == "__main__":
    test_quick_sort()
