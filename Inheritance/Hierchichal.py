class Parent:
    def earn(self):
        print('Parent Earning...')
  
    
class Child(Parent):  
    def play(self):
        print('Child Playing...')

class Child2(Parent):
    def cry(self):
        print('Grand Child crying...')
   

c=Child2()
c.earn()
c.play()
# c.cry()
