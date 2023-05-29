from abc import ABC, abstractmethod

from car import Car

class Battery(ABC, Car):

    @abstractmethod
    def needs_service(self):
        pass