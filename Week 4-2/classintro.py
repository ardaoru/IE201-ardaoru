i=5
def f():
    j=10
    print(j)

f()
class Apple:  # class, concept
    type = "fruit"    
    def __init__(self, loc = "tree", clr = "red"): # biz bir bilgi vermezsek default olarak bunları al
        self.location = loc
        self.color = clr

    def drop(self):
        if self.location == "tree":
            print("I dropped")
        else:
            print("I cannot be dropped")   

x = Apple("tree", "red") # object, tangible
y = Apple(loc = "ground")
z = Apple(clr = "yellow")

x.drop() # Actually calls Apple.drop(x)
y.drop()

print (x.type)