import random
import time

def hybridSort(L,S): #input array L and threshold S as parameters
    size=len(L)
    if size>S: #merge
        if size>1: #minimum size array atleast two elements
            L1 = L[:(size)//2]
            L2= L[size//2:]
            #divide into 2 equal sized sub arrays or problems
            #find solution to each of these sub problems
            if (len(L1)<=S):
                #switch to insertion sort
               insertion(L1)
            if (len(L2)<=S):
                insertion(L2)
                        
            if (len(L1)>S ) :
                L1 = hybridSort(L1,len(L1))
            if (len(L2)>S):
                L2 = hybridSort(L2,len(L2))
            
            L=merge(L1,L2)
        else:
            return
    else: # insertion
        insertion(L)
    return L

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
    L=[]
    kc=0
    while (L1 != [] and L2 != []):
        kc+=1
        if(L1[0]<L2[0]):
            L.append(L1[0])
            L1.remove(L1[0])
            print(L1,L2)
        elif(L2[0]<L1[0]):
            L.append(L2[0])
            L2.remove(L2[0])
        else: #the 1st element of 2 halves are equal
            if(len(L1)==1 or len(L2)==1): break
            L.append(L1[0])
            L.append(L2[0])
            L1.remove(L1[0])
            L2.remove(L2[0])
    if(L1==[]):
        # L.append(L1[0])
        L.append(L2[0])
        # L1.remove(L1[0])
        L2.remove(L2[0])
    elif (L2==[]):
        L.append(L1[0])
        L1.remove(L1[0])

    return L

arr = [14,40,28,31,3,15,17,51]
print(hybridSort(arr,1))
# print(merge([14,40,28,31],[3,15,17,51]))
