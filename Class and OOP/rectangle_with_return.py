class Rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath

    def area(self):
        return self.length*self.breath
    
    def perimeter(self):
        return 2*(self.length+self.breath)
     

l=int(input('Enter Length of rectangle: '))
b=int(input('Enter Breath of rectangle: '))
R1=Rectangle(l,b)
print(f'Area of rectangle :{R1.area()}')
print(f'Permeter of rectangle: {R1.perimeter()}')
        