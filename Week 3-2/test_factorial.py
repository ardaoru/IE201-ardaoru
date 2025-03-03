import factorial

def test_4():
    assert factorial.factorial(4) == 24
    
def test_N1():
    assert factorial.factorial(-1) == None