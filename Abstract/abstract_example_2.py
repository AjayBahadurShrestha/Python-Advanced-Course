from abc import * 

class Person(ABC):
    @abstractmethod
    def speak(self):
        print('Ajay Shrestha')

p1=Person()