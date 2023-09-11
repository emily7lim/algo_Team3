# to test for test case, type pytest in terminal
import Project1

threshold_5 = 5
threshold_100 = 100

def test_empty():
    # verify empty array works
    output = Project1.hybridSort([], threshold_100)
    assert output==[]

def test_small():
    # check algo for small array size works
    output = Project1.hybridSort([5,100,2,1,6,68,45,45656,4], threshold_100)
    assert output==[1,2,4,5,6,45,68,100,45656]

def test_low_threshold():
    # verify empty array works
    output = Project1.hybridSort([3,6,5,2,1,4,10], 2)
    assert output==[1,2,3,4,5,6,10]