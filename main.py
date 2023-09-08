class Students:

  def __init__(self, name, id):
    self.name = name
    self.id = id

  def showStudent(self):
    print(f"{self.name}'s id is {self.id}\n")


class Bachelor(Students):

  def showProfile(self):
    print(f"{self.name}'s id is a bachelor\n")


s = Students("Tahmid", 67)
s.showStudent()
t = Bachelor("Tanmoy", 33)
t.showStudent()
t.showProfile()