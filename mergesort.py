def merge(L1,L2):
    merged=[] #temp arr to str sorted
    kc=0
    if (type(L1) is tuple):
        L1,keys=L1
        kc+=keys
    if (type(L2) is tuple):
        L2,keys=L2
        kc+=keys
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

def MergeSort(L):
    mid = (len(L)-1)//2 #index to split at
    if (len(L)==0 or len(L)==1):
        return L,0
    else:
        x1 =  MergeSort(L[:(mid+1)])
        x2 =  MergeSort(L[(mid+1):])

    L,kc= merge(x1,x2)
    return L,kc


arr = [4,23,2,1,4,7,6]
print(MergeSort(arr))