i=5
def f():
    j=10
    print(j)

f()
class Apple:  # class, concept
    type = "fruit"      
    location = "tree" # should be different for each instance
    def drop(self):
        #if location == "tree":
         #   print("I dropped")
        #else
        print("I cannot dropped")   

x = Apple() # object, tangible
y = Apple()

x.drop() # Actually calls Apple.drop(x)

print (x.type)