
# selection sort algorithm
def selectionSort(n, arr):
    for i in range(n):
        mini = i
        # loop to get the minimum index from the array
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        # swap ith element with minimum value
        arr[i], arr[mini] = arr[mini], arr[i]

def main():
    # size of the array
    n = 8
    # array of elements
    arr = [8, 1, -4, 9, 3, -2, 5, 12]
    print("Array before sorting : ", arr)
    selectionSort(n, arr)
    print("Array after sorting : ", arr)

if __name__ == "__main__":
    main()
