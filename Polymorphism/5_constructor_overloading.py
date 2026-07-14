class ABC:
    def __init__(self):
        print('Constructor with 0 argument')
    def __init__(self,a):
        print('Constructor with 1 argument {a}')
    def __init__(self,a,b):
        print('Constructor with 2 argument {a} and {b}')
    def __init__(self,a,b,c):
        print('Constructor with 3 argument {a}, {b} and {c}')

obj =ABC(10,20,3)
