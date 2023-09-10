import janaki

threshold = 100

def test_empty():
    # verify empty array works
    output = janaki.hybridSort([], threshold)
    assert output==[]

def test_small():
    # check algo for small array size works
    output = janaki.hybridSort([5,100,2,1,6,68,45,45656,4], threshold)
    assert output==[1,2,4,5,6,45,68,100,45656]