from abc import ABC, abstractmethod


class Engine(ABC, Car):

    @abstractmethod
    def needs_service(self):
        pass