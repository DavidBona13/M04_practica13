
#School class to manage the schools of Georgia
class School:
    def __init__(self,
                 Faculty  , Facilities,
                 Type     , Name      ,
                 Location , Curriculum):
        self.Faculty    = Faculty
        self.Facilities = Facilities
        self.Type       = Type
        self.Name       = Name
        self.Location   = Location
        self.Curriculum = Curriculum

    #Print school embed data
    def Info(self):
        print("\nVehicle embed data")
        print(f"Faculty : {self.Faculty}")
        print(f"Facilities : {self.Facilities}")
        print(f"Type : {self.Type}")
        print(f"Name : {self.Name}")
        print(f"Location : {self.Location}")
        print(f"Curriculum : {self.Curriculum}\n")


    #The Getters start here

    def GetFaculty(self):
        return self.Faculty

    def GetFacilities(self):
        return self.Facilities

    def GetType(self):
        return self.Type

    def GetName(self):
        return self.Name

    def GetLocation(self):
        return self.Location

    def GetCurriculum(self):
        return self.Curriculum


    #The Setters start here

    def SetFaculty(self, NewFaculty):
        self.Faculty = NewFaculty

    def SetFacilities(self, NewFacilities):
        self.Facilities = NewFacilities

    def SetType(self, NewType):
        self.Type = NewType

    def SetName(self, NewName):
        self.Name = NewName

    def SetLocation(self, NewLocation):
        self.Location = NewLocation

    def SetCurriculum(self, NewCurriculum):
        self.Curriculum = NewCurriculum

    def SetReproduction(self, NewColor):
        self.Color = NewColor



