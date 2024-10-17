import random
import math

def initate_arr(n : int) :
    r = []
    for i in range(n):
        r.append(random.randint(1,100))
    return r

def show_arr(arr : list):
    for i in arr : print(i,end=' ')

def insertion_sort(arr : list):
    for i in range(1,len(arr)) :
        key = arr[i]
        j=i-1
        while j>=0 and arr[j]>key :
            arr[j+1]=arr[j]
            j -= 1
        arr[j+1] = key

def bubble_sort(arr : list) :
    n = len(arr)
    for i in range(n) :
        for j in range(n-i-1) :
            if arr[j]>arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def merge(arr:list,p:int,q:int,r:int):
    L = arr[p:q]
    R = arr[q:r]
    L.append(math.inf)
    R.append(math.inf)
    i = j = 0
    for k in range(p,r) :
        if  L[i]<=R[j] :
            arr[k]=L[i]
            i += 1
        else :
            arr[k]=R[j]
            j += 1

def merge_sort(arr :list, p :int, r :int):
    if p<r-1 :
        q = (p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q,r)
        merge(arr,p,q,r)

def partition(arr: list, p: int, q: int) -> int:
    key = arr[p]  # Use the first element of the subarray as the pivot
    j = p  # Pointer for the position of the smaller element
    for i in range(p + 1, q):  # Loop through the subarray
        if arr[i] < key:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]  # Swap elements to move smaller elements to the left
    arr[p], arr[j] = arr[j], arr[p]  # Place the pivot in its correct position
    return j  # Return the pivot index

def quicksort(arr: list, p: int, r: int):
    if p < r - 1:  # Stop when the range has one or zero elements
        q = partition(arr, p, r)
        quicksort(arr, p, q)       # Sort elements before pivot
        quicksort(arr, q + 1, r) 


