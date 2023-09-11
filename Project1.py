import random

def hybridSort(L,S):
    #we have input array and threshold S as parameters
    size=len(L)
    if size>S:
        #use mergesort
        
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
        else :
            return
    else:
        # insertion
        insertion(L)
    return L

def insertion(L):
    for i in range(1,len(L)):
            for j in range(i,0,-1):
                if L[j]<L[j-1]:
                    L[j],L[j-1] = L[j-1],L[j]
                else :
                    break

def merge(L1,L2):
    L=[]
    while (len(L1)!=0 or len(L2)!=0):
        if (len(L1)!=0 and len(L2)!=0 and L1[0]>L2[0]):
                L.append(L2[0])
                L2.remove(L2[0])
        elif (len(L1)!=0 and len(L2)!=0 and L2[0]>L1[0]):
            L.append(L1[0])
            L1.remove(L1[0])
        else:
            
            if ( len(L1)!=0 and len(L2)!=0):
                L.append(L1[0])
                L.append(L2[0])
                L1.remove(L1[0])
                L2.remove(L2[0])
            else :
                if (len(L1)==0 and len(L2)!=0):
                    while (len(L2)!=0):
                        L.append(L2[0])
                        L2.remove(L2[0])
                elif (len(L2)==0 and len(L1)!=0):
                    L.append(L1[0])
                    L1.remove(L1[0])
    return L

arr = [3,6,5,2,1,4,10]
print(hybridSort(arr, 2))
