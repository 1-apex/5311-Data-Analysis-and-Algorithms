from typing import TypeVar

T = TypeVar('T')

class Heap:
    
    heap: list[T] = []
    
    # constructor
    def __init__(self, arr: list[T]) -> None:
        self.heap = arr
    
    # Insert a new element into the heap (can be a part of building heap)
    def insertElement(self, value: T):
        # Add inserting value to the end of heap
        self.heap.append(value)
        
        # Index of the new inserted element
        i = len(self.heap) - 1
        parent = (i - 1) >> 1
        
        # Move the new element up until the heap property is restored
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) >> 1


    def heapify(self, n: int, i: int):
        # root
        smallest = i
        
        # children (normal math)
        # left = 2 * i + 1
        # right = 2 * i + 2
        
        # children (bitwise)
        left = (smallest << 1) + 1         
        right = (smallest << 1) + 2

        # check if the left child is smaller 
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left

        # check if the right child is smaller than the root
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        # if any of the right or left child is smaller -> we swap
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            # recursively call the same function so that the heap property is followed by the subtree too
            self.heapify(n, smallest)


    def build_min_heap(self):
        n = len(self.heap)
        # n//2-1 -> specifies the last non-leaf node
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
            
            
    def get_root(self) -> T:
        if (self.heap) == 0:
            return None
        else:
            return self.heap[0]
        
        
    def pop(self) -> T:
        if len(self.heap) == 0:
            return None
        
        # Swap root with the last element
        self.heap[0] = self.heap[-1]
        
        # remove the last elemtn (root --> swapped) 
        self.heap.pop()
        
        # Restore the heap property
        self.heapify(len(self.heap), 0)

    
if __name__ == '__main__':
    
    # --------------------------------------------------------------------------------------

    # BUILD MIN HEAP
    
    # Example 1
    # Initial array (max heap)
    arr = [50, 20, 30, 10, 15, 5, 25]
    heap = Heap(arr)
    heap.build_min_heap()    
    print(f'Min Heap : {heap.heap}\n')
    # Output: [5, 10, 25, 20, 15, 30, 50]
    
    # Example 2 (normal random array)
    arr = [4, 10, 3, 5, 1]
    heap = Heap(arr)
    heap.build_min_heap()
    print(f'Min Heap : {heap.heap}\n')
    # Output: [1, 4, 3, 5, 10]
    
    # Example 3 (min heap)
    arr = [1, 2, 3, 4, 5, 6, 7]
    heap = Heap(arr)
    heap.build_min_heap()
    print(f'Min Heap : {heap.heap}\n')
    # Output: [1, 2, 3, 4, 5, 6, 7]
    
    # Example 4 (integer array)
    arr = [7, 6, 5, 4, 3, 2, 1]
    heap = Heap(arr)
    heap.build_min_heap()
    print(f'Min Heap : {heap.heap}\n')
    # Output: [1, 3, 2, 4, 6, 7, 5]
    
    # Example 5 (float/double array)
    arr = [5.6, 2.3, 9.8, 7.1, 1.2, 4.5, 8.9]
    heap = Heap(arr)
    heap.build_min_heap()
    print(f'Min Heap : {heap.heap}\n')
    # Output: [1.2, 2.3, 4.5, 7.1, 5.6, 9.8, 8.9]
    
    # Example 6 (large integer array)    
    arr = [50, 20, 30, 10, 15, 5, 25, 70, 65, 60, 55, 85, 90, 40, 35, 100, 45, 80, 95, 75]
    heap = Heap(arr)
    heap.build_min_heap()
    print(f'Min Heap : {heap.heap}\n')
    # Output: [5, 10, 25, 20, 15, 30, 35, 45, 65, 60, 55, 85, 90, 40, 50, 100, 70, 80, 95, 75]
    
    # Example 7 (long (datatype) array)
    arr = [50123456789, 20123456789, 30123456789, 10123456789, 15123456789, 5123456789, 
           25123456789, 70123456789, 65123456789, 60123456789, 55123456789, 85123456789, 
           90123456789, 40123456789, 35123456789, 100123456789, 45123456789, 80123456789, 
           95123456789, 75123456789]
    heap = Heap(arr)
    heap.build_min_heap()
    print(f'Min Heap : {heap.heap}\n')
    # Output: [5123456789, 10123456789, 25123456789, 20123456789, 15123456789, 30123456789, 35123456789, 45123456789, 65123456789, 60123456789, 55123456789, 85123456789, 90123456789, 40123456789, 50123456789, 100123456789, 70123456789, 80123456789, 95123456789, 75123456789]
    
    # Example 8 (empty array)
    arr = []
    heap = Heap(arr)
    heap.build_min_heap()
    print(f'Min Heap : {heap.heap}')
    # Output: []
    
    # --------------------------------------------------------------------------------------
    
    # INSERT NEW NODE IN HEAP
    arr = [5, 10, 25, 20, 15, 30, 50]
    heap = Heap(arr)
    heap.insertElement(2)
    print("Heap after inserting 2:", heap.heap)
    # Output:  [2, 5, 25, 10, 15, 30, 50, 20]

    heap.insertElement(8)
    print("Heap after inserting 8:", heap.heap, "\n")
    # Output:  [2, 5, 25, 8, 15, 30, 50, 20, 10]
    
    # --------------------------------------------------------------------------------------
    
    # GET ROOT NODE
    arr = [9, 4, 7, 1, 3, 2, 6]
    print(f'Initital Array : {arr}')
    
    heap = Heap(arr)
    heap.build_min_heap()
    print(f'Heap formed : {heap.heap}')
    print(f'Root element : {heap.get_root()}\n')
    # Output: Heap formed : [1, 3, 2, 4, 9, 7, 6]
    #         Root element : 1
    
    # --------------------------------------------------------------------------------------
    
    # POP ROOT NODE 
    # arr = [9, 4, 7, 1, 3, 2, 6]
    # heap formed : [1, 3, 2, 4, 9, 7, 6] (reference line 170)
    heap.pop()
    print(f'Heap after root popped : {heap.heap}\n')
    # Output: [2, 3, 6, 4, 9, 7]
    
    # --------------------------------------------------------------------------------------
