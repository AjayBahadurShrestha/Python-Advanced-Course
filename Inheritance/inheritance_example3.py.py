class Parent:
    def __init__(self, pname, age, salary):
        self.pname=pname
        self.age=age
        self.salary=salary
    
    def displayP(self):
        print(f'Parent Name: {self.pname}')
        print(f'Parent Age: {self.age}')
        print(f'Parent Salary: {self.salary}')
        print('--'*30)
        print()
class Child(Parent):   #Is A relationship
    def __init__(self, cname, id, fees, pname, age, salary):
        super().__init__(pname,age,salary)
        self.cname=cname
        self.id=id
        self.fees=fees
    
    def displayC(self):
        super().displayP()
        print(f'Parent Name: {self.cname}')
        print(f'Parent Id: {self.id}')
        print(f'Parent Fees: {self.fees}')
        print('--'*30)
        print()

c=Child("Pcps college", 12, 900000, "Lbef College", 27, 20000000)
c.displayC()
