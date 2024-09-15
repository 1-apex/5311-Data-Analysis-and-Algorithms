def remove_duplicates(arr: list):
    j = 0
    result = [arr[j]]
    
    for i in range(len(arr)):
        if arr[i] != result[-1]:
            result.append(arr[i])
            j += 1
    
    return result

def main():
    arr = [2, 2, 2]
    distinct_elements = remove_duplicates(arr);
    print(distinct_elements)
    # Output: [2]
    
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    distinct_elements = remove_duplicates(arr);
    print(distinct_elements)
    # Output: [1, 2, 3, 4, 5]

if __name__ == '__main__':
    main()