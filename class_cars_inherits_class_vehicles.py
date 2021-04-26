"""
Details:
Create a class called "Vehicle" and methods that allow you to set the 
"Make", "Model", "Year,", and "Weight".
The class should also contain a "NeedsMaintenance" boolean that defaults
to False, and and "TripsSinceMaintenance" Integer that defaults to 0.
Next an inheritance classes from Vehicle called "Cars".

The Cars class should contain a method called "Drive" that sets the state of 
a boolean isDriving to True.  It should have another method called "Stop" that
sets the value of isDriving to false.

Switching isDriving from true to false should increment the
"TripsSinceMaintenance" counter. And when TripsSinceMaintenance
exceeds 100, then the NeedsMaintenance boolean should be set to true.
Add a "Repair" method to either class that resets the TripsSinceMaintenance
to zero, and NeedsMaintenance to false.

Create 3 different cars, using your Cars class, 
and drive them all a different number of times. 
Then print out their values for Make, Model, Year, Weight, NeedsMaintenance,
and TripsSinceMaintenance

"""
class Vehicle:

    def __init__(self, Make, Model, Year, Weight):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0
    
        
class Cars(Vehicle): #cars class inheritance Vehicle class

    def Driv(self):        
        self.isDriving  = True  
        self.NeedsMaintenance = False        
        print("need maintannce: ", self.NeedsMaintenance)
        for self.TripsSinceMaintenance in range(100):
            self.TripsSinceMaintenance+=1
            if self.TripsSinceMaintenance == 100:
                self.NeedsMaintenance = True               

    def Stop(self):
        self.isDriving = False   
        #print(self.isDriving)                    

    def Repair(self):
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0        
        print("** Car Repaired  **")        
        print("NeedsMaintenance: ", self.NeedsMaintenance, "|", "Trips Since Maintenance: ", self.TripsSinceMaintenance)
        

# Create 3 Cars 
ford = Cars("ford","foucs", "2020","1000")
GM = Cars("GM","Taho", "2020","1000")
Volvo = Cars("Volvo","CX90", "2020","1000")

# Ford as example 

ford.Driv() #start driving
print("** Driving started...**")
print("is Driving: ", ford.isDriving)
print("need maintannce: ",  ford.NeedsMaintenance)
print()

ford.Stop()  #stop driving
print("** Driving stoped **")
print("is Driving: ", ford.isDriving)
print("need maintannce: ",  ford.NeedsMaintenance)
print("Trips Since Maintenance: ", ford.TripsSinceMaintenance)
print()

ford.Repair() # repair the car

#Note: same can be applied for all cars