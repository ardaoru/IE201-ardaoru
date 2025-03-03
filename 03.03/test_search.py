import search

def test_1():
   assert search.SearchIterative_1([2, 5, 4], 8) == None

def test_2():
   assert search.SearchIterative_1([2, 5, 4], 5) == 1   

def test_3():
   assert search.SearchIterative_2([2, 5, 4], 8) == None

def test_4():
   assert search.SearchIterative_2([2, 5, 4], 5) == 1   


