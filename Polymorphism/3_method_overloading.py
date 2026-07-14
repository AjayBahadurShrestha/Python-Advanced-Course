class A:
    def walk(self):
        print(f'Walk with 0 argument')

class B(A):
    def walk(self,a,b,c):
        print(f'Walk 3 argument {a}, {b}, and {c}')

obj = B()
obj.walk(2,4,6)
