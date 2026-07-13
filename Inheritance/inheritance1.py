class Human:
    def walk(self):
        print("Human is walking...")
    def sleep(self):
        print("Sleeping")

class Student(Human):   #Is A relationship
    def read(self):
        print("Reading")

s=Student() 
s.read()
s.walk() #Has A relationship