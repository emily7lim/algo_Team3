import random
import time

def hybridSort(L, S):
    size = len(L)
    kc = 0
    if size > S:
        if size > 1:
            L1, kc1 = hybridSort(L[:(size) // 2], S)
            L2, kc2 = hybridSort(L[size // 2:], S)
            L, keys = merge(L1, L2)
            kc += kc1 + kc2 + keys
        else:
            return L, kc
    else:
        kc += insertion(L)
    return L, kc

def insertion(L):
    key_comparison = 0
    for i in range(1,len(L)):
        for j in range(i,0,-1):
            key_comparison += 1
            if L[j]<L[j-1]:
                L[j],L[j-1] = L[j-1],L[j]
            else:
                break
    return key_comparison

def merge(L1, L2):
    merged = []
    kc = 0
    i = j = 0
    while i < len(L1) and j < len(L2):
        kc += 1
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1
    merged.extend(L1[i:])
    merged.extend(L2[j:])
    return merged, kc

# Example usage:
# arr = [3, 6, 5, 11, 2, 1, 4, 10, 22, 60, 16, 23, 14, 15, 21]
# threshold = 2
# sorted_arr, comparisons = hybridSort(arr, threshold)
# print("Sorted Array:", sorted_arr)
# print("Key Comparisons:", comparisons)


# arr = [14,40,28,31,3,15,17,51]
# arr = [22,1,3,2,6,8,9]
# arr = [3,6,5,11,2,1,4,10,22,60,16,23,14,15,21]
arr = [5,5,5,5,5]
print(hybridSort(arr,1))
# print(insertion([3,5,1,6,2]))
# print(merge([14,40,28,31],[3,15,17,51]))
