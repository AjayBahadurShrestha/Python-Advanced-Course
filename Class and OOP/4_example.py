class Human:
    college = 'LBEF' #class variable
    def __init__(self,name,size,color):#name,size,color (local variable)
        self.name=name
        self.size=size          #self.name,self.size,self.color( instance variable)
        self.color=color
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")
        print(f"College: {Human.college}")
    
    @classmethod
    def walk(cls):
        print('This is class method')

    @staticmethod
    def widsh():
        print('Good Morning...')



h1=Human("Pappu Gupta",5,"Black & White")   #h1,h2(reference variiable)
Human.walk()
h1.walk()
h2=Human("Ramu Bohora",4,"Complexion")
h3=Human("Rijan Pariyar",3,"Gau goro")




h1.display()
print()
