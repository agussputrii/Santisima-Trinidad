class TriAthlete():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    style = "Triathlete"

    #Getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    #Setters
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age
    
    def __str__(self):
        return f"| Name: {self.name} || Age: {self.age} || Style: {self.style} |"

#CYCLIST CLASS
class Cyclist(TriAthlete):
    def __init__(self, name, age):
        super().__init__(name, age)#extended from TriAthlete
    
    style = "Cyclist"

    def __str__(self):
        return super().__str__()

#SWIMMER CLASS
class Swimmer(TriAthlete):
    def __init__(self, name, age):
        super().__init__(name, age)#extended from TriAthlete
    
    style = "Swimmer"

    def __str__(self):
        return super().__str__()

#RUNNER CLASS
class Runner(TriAthlete):
    def __init__(self, name, age):
        super().__init__(name, age)#extended from TriAthlete
    
    style = "Runner"

    def __str__(self):
        return super().__str__()


name = input("Enter the name: ")
age = int(input("Enter the age: "))

atleta1 = Cyclist(name, age)

name = input("Name: ")
age = int(input("Age: "))

atleta2 = Swimmer(name, age)

print(atleta1.__str__())
print(atleta2.__str__())





