def SearchIterative_1(ls, x):
    index = 0
    for i in ls:
        if i == x:
            return index
        index += 1
    return None     

def SearchIterative_2(ls, x):
    for index, i in enumerate(ls):
        if i == x:
            return index
    return None 