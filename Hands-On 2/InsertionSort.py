# Insertion Sort Algorithm
# ID: 1002233913
# Name: Prathamesh Patil

# Insertion sort algorithm
def insertionSort(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Insert the key to its correct position in the array
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    # Test Case 1: Standard array
    arr1 = [8, 1, -4, 9, 3, -2, 5, 12]
    insertionSort(len(arr1), arr1)
    print("Test Case 1:", arr1)
    
    # Test Case 2: Empty array
    arr2 = []
    insertionSort(len(arr2), arr2)
    print("Test Case 2:", arr2)
    
    # Test Case 3: Array with a single element
    arr3 = [3913]
    insertionSort(len(arr3), arr3)
    print("Test Case 3:", arr3)
    
    # Test Case 4: Sorted array - Ascending
    arr4 = [11, 29, 35, 79, 96]
    insertionSort(len(arr4), arr4)
    print("Test Case 4:", arr4)
    
    # Test Case 5: Sorted array - Descending
    arr5 = [834, 765, 666, 432, 321, 2]
    insertionSort(len(arr5), arr5)
    print("Test Case 5:", arr5)
    
    # Test Case 6: All identical elements
    arr6 = [7777, 7777, 7777, 7777]
    insertionSort(len(arr6), arr6)
    print("Test Case 6:", arr6)
    
if __name__ == "__main__":
    main()
