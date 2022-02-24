'''
Quicksort
divide and conquer alogirthm
How to pick a pivot
    Always pick first element as pivot
    Always pick last element as pivot
    Pick A random element as pivot
    Pick median as pivot
'''
from numpy import array


def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if (start < end):
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end

def quickSort(arr, start, end):
    if (start < end):
        p = partition(arr, start, end)
        quickSort(arr, start, p-1)
        quickSort(arr, p+1, end)
    
arr = [ 10, 7, 8, 9, 1, 5 ]
quickSort(arr, 0, len(arr) - 1)
print(arr)
