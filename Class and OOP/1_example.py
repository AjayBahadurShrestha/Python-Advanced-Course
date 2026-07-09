class Human:
    color='White'
    name='Ajay Bahadur Shrestha'
    size=13
    hand=2
    leg=2
    eye=2
    
    def walk(self):
        print('Human is walking...')
    
    def sleep(self):
        print('Human is sleeping...')
    
    def eat(self):
        print('Human is eating...')
    
    def bath(self):
        print('Human is bathing...')

h1=Human()
h2=Human()
h3=Human()


print(f"Name: {h1.name}")
print(f"Action: {h1.color}")
h1.bath()
