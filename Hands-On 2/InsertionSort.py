
# insertion sort algorithm
def insertionSort(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i-1
        # insert the key to its correct position in the array
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1 
        arr[j+1] = key

def main():
    # size of the array
    n = 8
    # array of elements
    arr = [8, 1, -4, 9, 3, -2, 5, 12]
    print("Array before sorting : ", arr)
    insertionSort(n, arr)
    print("Array after sorting : ", arr)

if __name__ == "__main__":
    main()
