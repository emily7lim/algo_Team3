import time
import random


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[left + i]

    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

        # copy any remaining elements of L[]
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copy any remaining elements of R[]
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):
    if left < right:

        mid = left+(right-left)//2  # get the int

        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)


# test code
arr = [random.randint(1, 50) for _ in range(0, 10)]
arrlen = len(arr)
print("Given array is")
for i in range(arrlen):
    print("%d" % arr[i], end=" ")

mergeSort(arr, 0, arrlen-1)
print("\n\nSorted array is")

# f = open('output.txt', 'w')
for i in range(arrlen):
    print("%d" % arr[i], end=" ")
#     f.write(str(arr[i]))
#     f.write("\n")
# f.close()

  
