class Person :
  def __init__(self , name , age , rank ):
    self.name = name
    self.age = age
    self.rank = rank

  def myfunc(self):
    print("Hello my name is  {}  i am {} my rank {} " .format(self.name , self.age , self.rank))


p1 = Person("Youssef", 36 , "tc")
p1.myfunc()

        