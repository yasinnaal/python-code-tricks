class Pet:

  def __init__(self,name):
    self.name = name

  def getName(self):
    return self.name

  def setName(self,x):
    self.name = x

myPet = Pet("Freddie")
print(myPet.name)
yourPet = Pet("Jack")
yourPet.setName("Bob")
print(myPet.getName())