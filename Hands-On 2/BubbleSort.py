# Bubble Sort Algorithm
# ID: 1002233913
# Name: Prathamesh Patil

# bubble sort algorithm
def bubbleSort(n, arr):
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # if the array is already sorted, return 
        if not swapped:
            return

def main():
    # Test Case 1: Standard array
    arr1 = [8, 1, -4, 9, 3, -2, 5, 12]
    bubbleSort(len(arr1), arr1)
    print("Test Case 1:", arr1)
    
    # Test Case 2: Empty array
    arr2 = []
    bubbleSort(len(arr2), arr2)
    print("Test Case 2:", arr2)
    
    # Test Case 3: Array with a single element
    arr3 = [3913]
    bubbleSort(len(arr3), arr3)
    print("Test Case 3:", arr3)
    
    # Test Case 4: Sorted array - Ascending
    arr4 = [11, 29, 35, 79, 96]
    bubbleSort(len(arr4), arr4)
    print("Test Case 4:", arr4)
    
    # Test Case 5: Sorted array - Descending
    arr5 = [834, 765, 666, 432, 321, 2]
    bubbleSort(len(arr5), arr5)
    print("Test Case 5:", arr5)
    
    # Test Case 6: All identical elements
    arr6 = [7777, 7777, 7777, 7777]
    bubbleSort(len(arr6), arr6)
    print("Test Case 6:", arr6)
    
if __name__ == "__main__":
    main()
