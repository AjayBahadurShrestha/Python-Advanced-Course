from random import *
print()
print("Welcome to our Guessing Number Application")
print('__'*30)
attempt=0
n=randint(1,100)
while True:
    guess= int(input('Enter your guess..[1-100]: '))

    if guess==n:
        attempt=attempt+1
        print(f"Congratulation!! You have guess it correctly in {attempt} times")
        break
    elif guess<n:
        print('value is greater...')
        attempt=attempt+1
    else:
        print('value is less...')
        attempt=attempt+1

    print('__'*30)
    print()
print('__'*30)
print()
