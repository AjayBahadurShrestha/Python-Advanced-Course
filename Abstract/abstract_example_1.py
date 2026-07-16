from abc import * 

class Person(ABC):
    def speak(self):
        print('Speak..')

    @abstractmethod
    def sucess(self):
        pass

class Student(Person):
    def sucess(self):
        print('Sucess by doing Smart and Hard work...')
    def mov(self):
        print('Moving...')


s1=Student()
s1.speak()
s1.sucess()
