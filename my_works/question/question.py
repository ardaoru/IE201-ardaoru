
# Quiz 1

"""Add necessary code to file `question.py` before the indicated line so that `Run()` function returns the following string as output:

>Istanbul => (BU, University), (ITU, University), (DSI, HighSchool, German), (GS, HighSchool, French); Konya => (Selcuk, University), (KAL, HighSchool, English)

Your code is expected to pass all the tests. You can use tests as hints, as well. Do not change the given code.

All your code should be written as classes in accordance with object oriented principles. Use polymorphism as much as possible."""

# City adlı bir class olmalı. School adlı bir class olmalı, bundan inheritance ile Univeristy ve high school beslenmeli

class City:
    def __init__(self, name):
        self.name = name
        self.schools = []		 

    def add_school(self, school):
        self.schools.append(school)

    def __str__(self):
        school_list = [str(school) for school in self.schools]
        text_format = ", ".join(school_list)
        return f"{self.name} => {text_format}"


class School:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"({self.name}, School)"


class University(School):
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"({self.name}, University)"


class HighSchool(School):
    def __init__(self,name,language):
        super().__init__(name)
        self.language = language

    def __str__(self):
        return f"({self.name}, HighSchool, {self.language})"
    

class Map:
    def __init__(self):
        self.cities = []
    
    def add_city(self, city):
        self.cities.append(city)
        return city

    def print(self):
        city_strings = [str(city) for city in self.cities]
        return "; ".join(city_strings)


# Add your code before this line. Do not change the code below this line.

def Run():
	m = Map()
	C1 = m.add_city(City("Istanbul"))
	C2 = m.add_city(City("Konya"))

	C1.add_school(University("BU"))
	C2.add_school(University("Selcuk"))
	C1.add_school(University("ITU"))
	C1.add_school(HighSchool("DSI", "German"))
	C1.add_school(HighSchool("GS", "French"))
	C2.add_school(HighSchool("KAL", "English"))

	return m.print()


print(Run())