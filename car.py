class Car:
    def __init__(self,brand,color,milage,isAutomatic):
        self.brand=brand
        self.color=color
        self.milage=milage
        self.isAutomatic=isAutomatic
    def display(self):
        print(self.brand)
        print(self.color)
        print(self.milage)
        if self.isAutomatic==True:
            print("Car is Auromtic")
        else:
            print("Car is not Manual")
carObj=Car("Volks Wagon","Blue","200kmph",True)
carObj.display()
