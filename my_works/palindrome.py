
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    my_str = str(x)
    y = len(my_str)

    if (y % 2) == 0:
        pass
    else:
        z = y/2 - 0.5
        z = int(z)
        my_str = my_str[:z]+my_str[z+1:]
        y = y-1

    t = int(y/2)

    str1 = my_str[0:t]
    str2 = my_str[t:y]
    str3 = str2[::-1]
    
    if str1 == str3:
        return True
    else:
        return False
    
num = 121
print(isPalindrome(num))




