class Rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath

    def area(self):
        print(f'Area of rectangle:{self.length*self.breath}')

    def perimeter(self):
        p=2*(self.length+self.breath)
        print(f'Perimeter of rectangle: {p}')

l=int(input('Enter Length of rectangle: '))
b=int(input('Enter Breath of rectangle: '))
R1=Rectangle(l,b)
R1.area()
R1.perimeter()
        