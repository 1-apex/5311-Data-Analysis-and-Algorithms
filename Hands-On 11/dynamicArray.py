class DynamicArray:
    def __init__(self, initial_capacity=2):
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * self.capacity

    def resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data

    def add(self, value):
        if self.size == self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of range")

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity


if __name__ == "__main__":
    arr = DynamicArray()

    # adding elements into dynamic array
    for i in range(10):
        arr.add(i)
        print(f"Added {i}, Size: {arr.get_size()}, Capacity: {arr.get_capacity()}")

    # checking the array
    try:
        for i in range(arr.get_size()):
            print(f"Element at index {i}: {arr.get(i)}")
    except IndexError as e:
        print(e)

    # trying to access out of bounds elements
    try:
        print(f"Element at index 20: {arr.get(20)}")
    except IndexError as e:
        print(e)


# EXPECTED OUTPUTS

# adding the elements output:
    # Added 0, Size: 1, Capacity: 2
    # Added 1, Size: 2, Capacity: 2
    # Added 2, Size: 3, Capacity: 4
    # Added 3, Size: 4, Capacity: 4
    # Added 4, Size: 5, Capacity: 8
    # Added 5, Size: 6, Capacity: 8
    # Added 6, Size: 7, Capacity: 8
    # Added 7, Size: 8, Capacity: 8
    # Added 8, Size: 9, Capacity: 16
    # Added 9, Size: 10, Capacity: 16
    
# checking the array output:
    # Element at index 0: 0
    # Element at index 1: 1
    # Element at index 2: 2
    # Element at index 3: 3
    # Element at index 4: 4
    # Element at index 5: 5
    # Element at index 6: 6
    # Element at index 7: 7
    # Element at index 8: 8
    # Element at index 9: 9
    
# output after trying to access the out of bounds index
    # Index out of range