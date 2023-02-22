
#Animal class to manage the farms of Georgia
class Animal:
    def __init__(self,
                 Specie  ,  Habitat ,
                 Diet    ,  Lifespan,
                 Behavior, Reproduction):
        self.Specie       = Specie
        self.Habitat      = Habitat
        self.Diet         = Diet
        self.Lifespan     = Lifespan
        self.Behavior     = Behavior
        self.Reproduction = Reproduction

    #Print animal embed data
    def Salutacio(self):
        print("\nAnimal embed data")
        print(f"Specie : {self.Specie}")
        print(f"Habitat : {self.Habitat}")
        print(f"Diet : {self.Diet}")
        print(f"Lifespan : {self.Lifespan}")
        print(f"Behavior : {self.Behavior}")
        print(f"Reproduction : {self.Reproduction}\n")


    #The Getters start here

    def GetSpecie(self):
        return self.Specie

    def GetHabitat(self):
        return self.Habitat

    def GetDiet(self):
        return self.Diet

    def GetLifespan(self):
        return self.Lifespan

    def GetBehavior(self):
        return self.Behavior

    def GetReproduction(self):
        return self.Reproduction


    #The Setters start here

    def SetSpecie(self, NewSpecie):
        self.Specie = NewSpecie

    def SetHabitat(self, NewHabitat):
        self.Habitat = NewHabitat

    def SetDiet(self, NewDiet):
        self.Diet = NewDiet

    def SetLifespan(self, NewLifespan):
        self.Lifespan = NewLifespan

    def SetBehavior(self, NewBehavior):
        self.Behavior = NewBehavior

    def SetReproduction(self, NewReproduction):
        self.Reproduction = NewReproduction



