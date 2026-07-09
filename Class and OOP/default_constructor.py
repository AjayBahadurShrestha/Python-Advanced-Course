class Human:
    college = 'LBEF' #class variable
    def __init__(self,):#name,size,color (local variable)
        self.name="Lbef"
        self.size=27         #self.name,self.size,self.color( instance variable)
        self.color='White'
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")
        print(f"College: {Human.college}")
    

h1=Human()   #h1,h2(reference variiable)
h2=Human()





h1.display()
print()
h2.display()
