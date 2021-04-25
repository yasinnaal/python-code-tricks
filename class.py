class Person:
  def __init__(self,name="Person",age=18):
    self.name = name
    self.age = age

  def DefinePersonAge(self,PersonAge):
    self.age = PersonAge

newPerson = Person("George",21)
newPerson.DefinePersonAge(18)
print(newPerson.name,newPerson.age)