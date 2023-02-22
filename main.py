
#imports tese
import animal
import vehicle
import school

#Function initialization and calls

#Animal
Lion = animal.Animal("Lion",
                "Savanna",
                "Carnivore",
                "10-14 yrs",
                "Social, Diurnal",
                "Viviparous")
#Vehicle
Toyota = vehicle.Vehicle("Toyota",
                "Camry",
                "Sedan",
                "Gasoline",
                "110mph",
                "Red")
#School
JamesMadison = school.School(50,
                "Library, Science Lab",
                "High School",
                "James Madison High School",
                "Arlington, Virginia",
                "Science, Mathematics, Language Arts, Social Studies")

#Animal class routine
animal.Animal.Salutacio(Lion)

animal.Animal.SetDiet(Lion ,"Herbibore")

animal.Animal.Salutacio(Lion)

#Vehicle class routine
vehicle.Vehicle.Parts(Toyota)

vehicle.Vehicle.SetFuel(Toyota ,"Diesel")

vehicle.Vehicle.Parts(Toyota)

#School class routine
school.School.Info(JamesMadison)

school.School.SetLocation(JamesMadison ,"Espana, Barcelona")

school.School.Info(JamesMadison)

