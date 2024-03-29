# This file tests all the testcase that we can possibly think of, there may be repeated testcase but with different values in array, just to double check.
# To test for test case, type pytest in terminal
import draft.Project1 as Project1
import mergesort

threshold_1 = 1
threshold_5 = 5 #size>5 for merge
threshold_10 = 10
threshold_100 = 100 #size<100 for insertion

# -------------- test for key comparison indiv fn ------------------
def test_insert_kc():
    # for insertion sort
    output = Project1.insertion([3,6,5,2,1,4,10])
    assert output == 14

def test_merge_kc():
    # for merge sort
    output = Project1.merge([5,14,17,51],[1,2,3,20,99])
    assert output == ([1,2,3,5,14,17,20,51,99],8)

def test_merg_samei():
    # for merge sort
    output = Project1.merge([4],[4])
    assert output == ([4,4], 1)

def test_merg_same():
    # for merge sort
    output = Project1.merge([4,8],[4,8])
    assert output == ([4,4,8,8], 2)

def test_merge_empty():
    # for merge sort
    output = Project1.merge([],[1,2,3,20,99])
    assert output == ([1,2,3,20,99],0)

def test_merg_empt():
    # for merge sort
    output = Project1.merge([2,4,80,90],[])
    assert output == ([2,4,80,90],0)

# -------------- test for arrays ------------------
def test_empty():
    # verify empty array works
    output = Project1.hybridSort([], threshold_100)
    assert output==([],0)

def test_empt():
    # verify empty array works
    output = Project1.hybridSort([], threshold_5)
    assert output==([],0)

def test_odd5():
    # verify odd array, merge to insertion works
    output = Project1.hybridSort([22,1,3,2,6,8,9], threshold_5)
    assert output==([1,2,3,6,8,9,22],12)

def test_even5():
    # verify even array, merge to insertion works
    output = Project1.hybridSort([22,1,3,2,6,8], threshold_5)
    assert output==([1,2,3,6,8,22],10)

def test_odd10():
    # verify odd array, insertion works
    output = Project1.hybridSort([22,1,3,2,6,8,9], threshold_10)
    assert output==([1,2,3,6,8,9,22],12)

def test_even10():
    # verify even array, insertion works
    output = Project1.hybridSort([22,1,3,2,6,8], threshold_10)
    assert output==([1,2,3,6,8,22],10)

def test_duplicate():
    output = Project1.hybridSort([2,1,4,2],threshold_5)
    assert output == ([1,2,2,4],4)

def test_duplicat():
    output = Project1.hybridSort([2,1,4,2],threshold_1)
    assert output == ([1,2,2,4],4)

def test_duplicate_al():
    output = Project1.hybridSort([5,5,5,5,5],threshold_1)
    assert output == ([5,5,5,5,5],5)

def test_duplicate_all():
    output = Project1.hybridSort([5,5,5,5,5],threshold_10)
    assert output == ([5,5,5,5,5],4)

# -------------- test for hybridsort ------------------
def test_small():
    # goes to only insertion sort
    output = Project1.hybridSort([5,100,2,1,6,68,45,45656,4], threshold_100)
    assert output==([1,2,4,5,6,45,68,100,45656],21)

def test_hybrid_kc():
    # goes to only insertion sort
    output = Project1.hybridSort([3,6,5,2,1,4,10],threshold_100)
    assert output == ([1,2,3,4,5,6,10],14)

def test_low_threshold():
    # merge then insertion
    output = Project1.hybridSort([3,6,5,11,2,1,4,10,22,60,16,23,14,15,21], threshold_5)
    assert output==([1,2,3,4,5,6,10,11,14,15,16,21,22,23,60],46)




# -------------- test for original mergesort ------------------
def test_mergesort():
    # for merge sort
    output = mergesort.origMergeSort([14,40,28,31,3,15,17,51])
    assert output == ([3,14,15,17,28,31,40,51],16)

def test_mergesort_odd():
    # for merge sort
    output = mergesort.origMergeSort([4,23,2,1,5,7,6])
    assert output == ([1,2,4,5,6,7,23],13)

def test_mergesort_duplicate():
    # for merge sort
    output = mergesort.origMergeSort([4,23,2,1,4,7,6])
    assert output == ([1,2,4,4,6,7,23],13)

def test_mergesort_empty():
    # for merge sort
    output = mergesort.origMergeSort([])
    assert output == ([],0)

def test_mergesort_one():
    # for merge sort
    output = mergesort.origMergeSort([1])
    assert output == ([1],0)