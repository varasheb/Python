from abc import ABC, abstractmethod

# Abstract base class ABC
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")

    def stop_engine(self):
        print("Motorcycle engine stopped")

car = Car()
motorcycle = Motorcycle()

car.start_engine()       
car.stop_engine()        

motorcycle.start_engine()  
motorcycle.stop_engine()   
