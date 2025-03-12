i=5
def f():
    j=10
    print(j)

f()
class Apple:  # class, concept
    type = "fruit"    
    def __init__(self, loc = "tree", clr = "red"): # biz bir bilgi vermezsek default olarak bunları al
        self._location = loc
        self._color = clr

    def _setlocation(self, l):
        self._location = l

    def drop(self):
        if self.location == "tree":
            print("I dropped")
        else:
            print("I cannot be dropped")   

x = Apple("tree", "red") # object, tangible -- init burada call edildiği için public olmalı
y = Apple(loc = "ground")
z = Apple(clr = "yellow")

z._color = "black" # acces to member variable. Should not be allowed.
z.drop() # if I designate drop function as pubic then ok. Otherwise should not be allowed.

x.drop() # Actually calls Apple.drop(x)
y.drop()

print (x.type)