
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
    # size of the array
    n = 8
    # array of elements
    arr = [8, 1, -4, 9, 3, -2, 5, 12]
    print("Array before sorting : ", arr)
    bubbleSort(n, arr)
    print("Array after sorting : ", arr)

if __name__ == "__main__":
    main()
