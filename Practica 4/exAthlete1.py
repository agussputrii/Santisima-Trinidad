################### CYCLIST #####################
class Cyclist:
    #Builder
    def __init__(self, style):
        self.__style = style

    #Father's method
    def doBike(self):
        print("im riding a bike LOOOOL")

    #toString
    def __str__(self):
        return f"Im a cyclist from style {self.__style}"

    #Getters
    def get_style(self):
        return self.__style

    #Setters
    def set_style(self, style):
        self.__style = style

################################ RUNNER ########################################

class Runner:
    #Builder
    def __init__(self, meters, type):
        self.__meters = meters
        self.__type = type

    #Father's methods
    def doRun(self):
        print("Im runningggggggg")

    #toString
    def __str__(self):
        return f"Im a runner of {self.__meters} of type {self.__type}"

    #Getters
    def get_meters(self, meters):
        return self.__meters

    def get_type(self, type):
        return self.__type
        
    #Setters
    def set_meters(self, meters):
        self.__meters = meters

    def set_type(self, type):
        self.__type = type

##################################### SWIMMER #######################################
class Swimmer:
    #Builder
    def __init__(self, style):
        self.__style = style

    #Father's methods
    def doSwim(self):
        return("Im swimming glub glub glub")

    #toString
    def __str__(self):
        return f"Im a swimmer from style {self.__style}"

    #Getters
    def get_style(self, style):
        return self.__style

    #Setters
    def set_style(self, style):
        self.__style = style


##################################### SON'S CLASS #######################################
class Triathlete(Cyclist, Runner, Swimmer):
    #Builder
    def __init__(self, styleS, meters, type, name_surname, age, style):
        Swimmer.__init__(self,styleS)
        Runner.__init__(self, meters, type)
        Cyclist.__init__(self, style)

        self.__name_surname = name_surname
        self.__age = age

    def __str__(self):
        return Swimmer.__str__(self) +"\n"+ Runner.__str__(self) +"\n"+ Cyclist.__str__(self)+"\n"+ f"My name is {self.__name_surname} and I'm {self.__age} years old"

##################################### MAIN #######################################
athlete1 = Triathlete("freestyle", "20", "short", "Carl Johnson", "30", "freestyle")
athlete2 = Triathlete("Butterfly", "40", "long", "Gordo Lolero", "19", "Mountain")
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n"+athlete1.__str__())
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n"+athlete2.__str__())