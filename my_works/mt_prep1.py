"""def sum_of_digits(n):
  if n == 0:
    return 0
  
  return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(376))"""



"""def count_digits(n):
    if n == 0:
        return 0
    
    return 1 + count_digits(n // 10)

print(count_digits(35644333))"""



"""def is_palindrome(s):
    if s[0] != s[-1]:
        return False
    if len(s) == 1:
        return True
    
    return is_palindrome(s[1:-1])

print(is_palindrome("asasadsa"))"""




"""def find_max(my_list):
    if len(my_list) == 1:
        return my_list[0]
    
    y = my_list[1:]
    return max(my_list[0], find_max(y))

print(find_max([3, 7, 1, 9, 5]))"""





"""Write a recursive python function called get_permutations that, given an input string, returns the list of all strings that can be obtained as permutations of characters of the given string. Write the code to a file named getpermutations.py.
Write a pytest test to make sure that input 'abc' returns ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'].
Write and explain the time complexity of function get_permutations in a file named q2.q3.md."""


"""def get_permutations(str):
    if len(str) <= 1:
        return str
   
    perms = []
   
    for i, char in enumerate(str):
        remaining = str[:i] + str[i+1:]
        for p in get_permutations(remaining):
            perms.append(char + p)
    return perms

print(get_permutations("abc"))"""



"""class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def info(self):
        print(f"Title: {self.title}, Author: {self.author}")


book1 = Book("1984", "George Orwell")
book1.info()"""


"""class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"Brand:{self.brand}, Year:{self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand,year)
        self.model = model

    def info(self):
        print(f"Brand:{self.brand}, Year:{self.year}, Model:{self.model}")


mycar = Car("Toyota", 2020, "Corolla")
mycar.info() """





"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm student {self.name} and I'm {self.age} years old.")   

class Student(Person):

    student_count = 0

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        Student.student_count +=1

    def introduce(self):
       print(f"Hi, I'm student {self.name} (ID:{self.student_id}) and I'm {self.age} years old.")


s1 = Student("Ali", 21, "S12345")
s2 = Student("Zeynep", 22, "S67890")

s1.introduce()
s2.introduce()

print(Student.student_count)"""





"""
class Shape:
    def __init__(self):
        pass
    def area(self):
        return "Unknown area"
    
    def __str__(self):
        return "Generic Shape"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __str__(self):
       return f"Rectangle ({self.width} x {self.height})" 
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    
    def __str__(self):
        return f"Circle (radius = {self.radius})"
    

shapes = [
    Rectangle(3, 4),
    Circle(5),
    Shape()]

for shape in shapes:
    print(shape.area())
    print(shape)"""



"""
def reverse_print(lst):
    if len(lst) == 1:
        return [lst[0]]
    
    rest = reverse_print(lst[:-1])

    return [lst[-1]] + rest

print(reverse_print([1, 2, 3]))"""



"""
def reverse_print(lst):
    if len(lst) == 1:
        return [lst[0]]
    
    rest = reverse_print(lst[1:])

    return  rest + [lst[0]] 

print(reverse_print([1, 2, 3]))"""




"""
def reverse_string(s):
    if len(s) == 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))"""



"""

def is_palindrome(s):
    lst = list(s)
    if len(lst) <= 1:
        return True
    
    if lst[0] != lst[-1]:
        return False
    
    return is_palindrome(lst[1:-1])

print(is_palindrome("1221"))"""




"""
def count_digits(n):
    if n < 10:
        return 1
    
    return count_digits(n // 10) + 1


print(count_digits(1234))"""




"""
result = []
for x in range(5):
    if x % 2 == 0:
        result.append(x)"""

"""
result = [x for x in range(5) if x % 2 == 0]
print(result)"""




"""
result = []
for x in range(5):
    if x % 2 == 0:
        result.append("even")
    else:
        result.append("odd")"""
"""
result = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(result)"""




"""
result = []
for x in [1, 2]:
    for y in [3, 4]:
        result.append((x, y)) """
"""
result = [(x,y) for x in [1,2] for y in [3,4]]
print(result) """






