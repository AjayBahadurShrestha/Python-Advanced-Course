
name = input("Enter student name: ")
age = int(input('Enter student age: '))
fees = float(input('Enter students fees: '))
f = open('xyz.txt', 'w')
f.write(f'{name} {age} {fees}')
f.close()
print('Data written succesfully !!')