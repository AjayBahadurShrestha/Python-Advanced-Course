from random import *

l=['Mango', 'Orange', 'Apple', 'Banana', 'Pineapple', 'Papaya']
print(choice(l))
print(choices(l,k=3))
print(sample(l,k=5))
(shuffle(l))
print(l)