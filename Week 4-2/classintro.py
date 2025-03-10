i=5
def f():
    j=10
    print(j)

f()
class Apple:  # class, concept
    type = "fruit"      
    location = "tree" # should be different for each instance
    def drop(self, l):
        self.location = l
        if self.location == "tree":
            print("I dropped")
        else:
        print("I cannot be dropped")   

x = Apple() # object, tangible
y = Apple()

x.drop("tree") # Actually calls Apple.drop(x)

print (x.type)