def merge_two_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []
    
    # Two-pointer technique to merge two sorted arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append the remaining elements of arr1 or arr2
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

def sort(k: int, n: int, arr1: list, arr2: list, arr3: list):
    arrays = [arr1, arr2, arr3]
    
    while len(arrays) > 1:
        merged_arrays = []
        
        # Merge arrays in pairs
        for i in range(0, len(arrays), 2):
            if i + 1 < len(arrays):
                merged_arrays.append(merge_two_arrays(arrays[i], arrays[i + 1]))
            else:
                merged_arrays.append(arrays[i])
        
        arrays = merged_arrays
        # print(f"After one pass of merging: {arrays}")
    
    return arrays[0]
    

def main():
    # subquestion 1
    k = 3
    n = 4
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    arr3 = [0, 9, 10, 11]
    
    sorted_array = sort(k, n, arr1, arr2, arr3)
    print(sorted_array)
    # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    # subquestion 2
    k = 3
    n = 3
    arr1 = [1, 3, 7]
    arr2 = [2, 4, 8]
    arr3 = [9, 10, 11]
    
    sorted_array = sort(k, n, arr1, arr2, arr3)
    print(sorted_array)
    # Output: [1, 2, 3, 4, 7, 8, 9, 10, 11]

if __name__ == "__main__":
    main()