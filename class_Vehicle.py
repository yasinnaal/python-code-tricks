class Vehicle:

    def __init__(self, type, id):
        self.type = type
        self.id = id

    def __str__(self):
      return ("The vehicle is a " + self.type)

class Car(Vehicle):

    def __init__(self, carID, color, type="car"):
        Vehicle.__init__(self, type, carID)
        self.color = color

    def __str__(self):
      return ("The vehicle is " + self.color)

newCar = Car("abc1234","red")
