
def ListSumRecursive(x):
    if not x:
        return 0
    
    return x[0] + ListSumRecursive(x[1:])