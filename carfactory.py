from abc import ABC, abstractmethod

from car import Car
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class CarFactory(ABC):
    
    def create_calliope(self, last_service_date, current_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(self.current_mileage, self.last_service_mileage), SpindlerBattery(self.last_service_date, self.current_date))

    def create_glissade(self, last_service_date, current_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(self.current_mileage, self.last_service_mileage), SpindlerBattery(self.last_service_date, self.current_date))

    def create_palindrome(self, last_service_date, current_date, warning_light_is_on):
        return Car(SternmanEngine(self.warning_light_is_on), NubbinBattery(self.last_service_date, self.current_date))

    def create_rorschach(self, last_service_date, current_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(self.current_mileage, self.last_service_mileage), NubbinBattery(self.last_service_date, self.current_date))

    def create_thovex(self, last_service_date, current_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(self.current_mileage, self.last_service_mileage), NubbinBattery(self.last_service_date, self.current_date))
        
