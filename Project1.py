import random
import time

def hybridSort(L,S): #input array L and threshold S as parameters
    size=len(L)
    kc=0
    if size>S: #merge
        if size>1: #minimum size array atleast two elements
            #divide into 2 equal sized sub arrays or problems
            #find solution to each of these sub problems
            L1 = L[:(size)//2]
            L2= L[size//2:]

            if (len(L1) <= S):
                #switch to insertion sort
               kc+=insertion(L1)
               print(kc,"II")
            if (len(L2) <= S):
                kc+=insertion(L2)
                print(kc,"&")
            if (len(L1) > S):
                print(L1)
                L1,keym = hybridSort(L1,len(L1))
                kc+=keym
            if (len(L2) > S):
                L2, keym = hybridSort(L2,len(L2))
                kc+=keym
            print(L1,L2)
            L,keys=merge(L1,L2)
            kc+=keys
        else:
            return
    else: # insertion
        kc+=insertion(L)
    # print(kc)
    return L,kc

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

def merge(L1,L2):
    L=[] #temp arr to str sorted
    kc=0
    while (L1 != [] and L2 != []):
        kc+=1
        if(L1[0]<L2[0]):
            modifyArray(L,L1)
        elif(L2[0]<L1[0]):
            modifyArray(L,L2)
        else: #the 1st element of 2 halves are equal
            modifyArray(L,L1)
            modifyArray(L,L2)
    while (L1 != [] or L2 != []):
        if(L1==[]):
            modifyArray(L,L2)
        elif (L2==[]):
            modifyArray(L,L1)
    return L,kc

def modifyArray(L, arr):
    L.append(arr[0])
    arr.remove(arr[0])

# arr = [14,40,28,31,3,15,17,51]
# arr = [22,1,3,2,6,8,9]
# arr = [3,6,5,11,2,1,4,10,22,60,16,23,14,15,21]
arr = [2,1,4,2]
print(hybridSort(arr,1))
# print(insertion([3,5,1,6,2]))
# print(merge([14,40,28,31],[3,15,17,51]))
