class Car :
    def __init__(self , speed , color , energypower , model ) :
        self.speed = speed
        self.color = color
        self.energypower = energypower
        self.model = model
    def info(self) :
        print("the speed car is {} km/h color {} energypower {} model {} " .format(self.speed , self.color ,self.energypower , self.model ))
c = Car (355 , "black" , " 600-horsepower ", "RS7") 
c.info()
print(c)