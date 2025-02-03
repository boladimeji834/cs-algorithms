# This program implements the quicksort algorithm 

def quicksort(array): 
    # logic to check take care of the end of the recursion
    # it does the conquer once the len of the array from the divide is 1 or 0
    if len(array) <= 1: return array 

    # the indexer to index the middle element of the array
    pivot = len(array) // 2

    # the divide stage to separate the array into three
    left = [num for num in array if num < array[pivot]]
    right = [num for num in array if num > array[pivot]]
    mid = [num for num in array if num == array[pivot]]

    # call the function again to continue doing the conquer untill the len <= 1
    return quicksort(left) + mid + quicksort(right)


if __name__ == "__main__": 
    print(quicksort([7, 3, 99, 57, 94, 74]))