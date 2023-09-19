def merge(L1,L2):
    L=[] #temp arr to str sorted
    kc=0
    if (type(L1) is tuple):
        L1,keys=L1
        kc+=keys
    if (type(L2) is tuple):
        L2,keys=L2
        kc+=keys

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
    # return L

def modifyArray(L, arr):
    L.append(arr[0])
    arr.remove(arr[0])

def MergeSort(L):
    mid = (len(L)-1)//2 #index to split at
    if (len(L)==0 or len(L)==1):
        return L,kc
    else:
        x1 =  MergeSort(L[:(mid+1)])
        x2 =  MergeSort(L[(mid+1):])

    L,kc= merge(x1,x2)
    return L,kc


arr = [4,23,2,1,5,7,6]
print(MergeSort(arr))