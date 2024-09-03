# Selection Sort Algorithm
# ID: 1002233913
# Name: Prathamesh Patil

# Selection sort algorithm
def selectionSort(n, arr):
    for i in range(n):
        mini = i
        # Loop to get the minimum index from the array
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        # Swap ith element with minimum value
        arr[i], arr[mini] = arr[mini], arr[i]

def main():
    # Test Case 1: Standard array
    arr1 = [8, 1, -4, 9, 3, -2, 5, 12]
    selectionSort(len(arr1), arr1)
    print("Test Case 1:", arr1)
    
    # Test Case 2: Empty array
    arr2 = []
    selectionSort(len(arr2), arr2)
    print("Test Case 2:", arr2)
    
    # Test Case 3: Array with a single element
    arr3 = [3913]
    selectionSort(len(arr3), arr3)
    print("Test Case 3:", arr3)
    
    # Test Case 4: Sorted array - Ascending
    arr4 = [11, 29, 35, 79, 96]
    selectionSort(len(arr4), arr4)
    print("Test Case 4:", arr4)
    
    # Test Case 5: Sorted array - Descending
    arr5 = [834, 765, 666, 432, 321, 2]
    selectionSort(len(arr5), arr5)
    print("Test Case 5:", arr5)
    
    # Test Case 6: All identical elements
    arr6 = [7777, 7777, 7777, 7777]
    selectionSort(len(arr6), arr6)
    print("Test Case 6:", arr6)
    
if __name__ == "__main__":
    main()
