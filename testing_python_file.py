#testing python code
from typing import List

def insertion_sort1(arr: List[int])->list:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

def insersion_sort2(collection:list) -> list:
    for insert_index, insert_value in enumerate(collection[1:]):
        while insert_index >= 0 and insert_value < collection[insert_index]:
            collection[insert_index], collection[insert_index+1] =collection[insert_index+1], collection[insert_index]
            insert_index -= 1
    return collection
        
    
def insersion_sort3(collection:list)->list:
    for i in range(1, len(collection)):
        for j in range(i-1, -1, -1):
            if j >= 0 and collection[i] < collection[j]:
                collection[i], collection[j] = collection[j], collection[i]
                if i > 1:
                    i -= 1
    return collection

# bitonic sort with sequential programming
# compare and swap : compare two indexes then swap them if they meet the condition or direction
def comp_and_swap(collection:List, index1:int, index2:int, direction:int) -> None:
    """
        >> input = [5, 8, 1, 6]
        >> comp_and_swap(input, 0, 1, 0)
        >> [8, 5, 1, 6]
        
    """
    if (direction == 0 and (collection[index1] < collection[index2])) or (direction == 1 and (collection[index1] > collection[index2])):
        collection[index1], collection[index2] = collection[index2], collection[index1]


# merge bitonic array
def bitonic_merge(collection:List, low:int, length:int, direction:int) -> None:
    """
        >>> arr = [12, 42, -21, 1]
        >>> bitonic_merge(arr, 0, 4, 1)
        >>> print(arr)
        [-21, 1, 12, 42]
    """

    if length > 1:
        middle:int = int(length/2)
        for i in range(low, low + middle):
            comp_and_swap(collection, i, i + middle, direction)
        bitonic_merge(collection, low, middle, direction)
        bitonic_merge(collection, low+middle, middle, direction)
            
# bitonic sort 
def bitonic_sort(collection:List, low:int, length:int, direction:int) -> None:
    #     >>> arr = [12, 34, 92, -23, 0, -121, -167, 145]
    #     >>> bitonic_sort(arr, 0, 8, 1)
    #     >>> arr
    #     [-167, -121, -23, 0, 12, 34, 92, 145]
    
    if length > 1:
        middle = int(length/2)
        bitonic_sort(collection, low, middle, 1)
        bitonic_sort(collection, low+middle, middle, 0)
        bitonic_merge(collection, low, length, direction)
    

if __name__ == '__main__':
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item.strip()) for item in user_input.split(",")]

    bitonic_sort(unsorted, 0, len(unsorted), 1)
    print("\nSorted array in ascending order is: ", end="")
    print(*unsorted, sep=", ")

    bitonic_merge(unsorted, 0, len(unsorted), 0)
    print("Sorted array in descending order is: ", end="")
    print(*unsorted, sep=", ")