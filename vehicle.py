
#Vehicle class to manage the garages of Georgia
class Vehicle:
    def __init__(self,
                 Manufacturer,  Model,
                 Type        ,  Fuel ,
                 Speed       , Color):
        self.Manufacturer = Manufacturer
        self.Model        = Model
        self.Type         = Type
        self.Fuel         = Fuel
        self.Speed        = Speed
        self.Color        = Color

    #Print vehicle embed data
    def Parts(self):
        print("\nVehicle embed data")
        print(f"Manufacturer : {self.Manufacturer}")
        print(f"Model : {self.Model}")
        print(f"Type : {self.Type}")
        print(f"Fuel : {self.Fuel}")
        print(f"Speed : {self.Speed}")
        print(f"Color : {self.Color}\n")


    #The Getters start here

    def GetManufacturer(self):
        return self.Manufacturer

    def GetModel(self):
        return self.Model

    def GetType(self):
        return self.Type

    def GetFuel(self):
        return self.Fuel

    def GetSpeed(self):
        return self.Speed

    def GetColor(self):
        return self.Color


    #The Setters start here

    def SetManufacturer(self, NewManufacturer):
        self.Manufacturer = NewManufacturer

    def SetModel(self, NewModel):
        self.Model = NewModel

    def SetType(self, NewType):
        self.Type = NewType

    def SetFuel(self, NewFuel):
        self.Fuel = NewFuel

    def SetSpeed(self, NewSpeed):
        self.Speed = NewSpeed

    def SetReproduction(self, NewColor):
        self.Color = NewColor



