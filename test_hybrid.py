# to test for test case, type pytest in terminal
import Project1

threshold_5 = 5 #for insertion
threshold_100 = 100 #for merge

# -------------- test for key comparison ------------------
def test_insert_kc():
    # for insertion sort
    output = Project1.insertion([3,6,5,2,1,4,10])
    assert output == 14

# def test_merge_kc():
#     # for merge sort
#     output = Project1.hybridSort([14,40,28,31,3,15,17,51],threshold_5)
#     assert output == 9

# def test_merg_kc():
#     # for merge sort
#     output = Project1.hybridSort([90,25,10,71,94,22,59,74],threshold_5)
#     assert output == 17

# -------------- test for arrays ------------------
def test_empty():
    # verify empty array works
    output = Project1.hybridSort([], threshold_100)
    assert output==[]

def test_empt():
    # verify empty array works
    output = Project1.hybridSort([], threshold_5)
    assert output==[]

# -------------- test for insertionsort ------------------
def test_small():
    # check algo for small array size works
    output = Project1.hybridSort([5,100,2,1,6,68,45,45656,4], threshold_100)
    assert output==[1,2,4,5,6,45,68,100,45656]

def test_low_threshold():
    # verify low threshold works
    output = Project1.hybridSort([3,6,5,2,1,4,10], 2)
    assert output==[1,2,3,4,5,6,10]

# -------------- test for mergesort ------------------
