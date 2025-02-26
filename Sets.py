# Sets:

x = {12, "tamer"}
y = {13, 67, 13, 99} #set içerisinde unique değerler var

# Dictionaries:
z = {"q":6, "w":45, "e": "tamer", "p":6}

# Dictionary nasıl iterate edilir mutlaka bak!!!

x1, x2 = x

# List comprehansion
listofsquares = []
for i in range(11):
    listofsquares.append(i**2)

# YA DA

los = [i**2 for i in range(1,11)]

# Bir değerin varlığını kontrol
result = 25 in y
print(result)

# YA DA
b = False
for i in y:
    if i == 25:
        b = True    
        break

def f():
    return 10