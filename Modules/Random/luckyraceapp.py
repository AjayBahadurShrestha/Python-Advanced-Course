from random import*
import time
player1='Ronaldo'
player2='Messi'
player3='Kylien Mbappe'
player4='Haaland'
r=m=k=h=0

print()
print("Welcome to our Lucky Race")
print("__"*30)
while True:
    n=randint(1,6)
    print(f"{player1}: {n}")
    r=r+n
    time.sleep(2)
    
    n=randint(1,6)
    print(f"{player2}: {n}")
    m=m+n
    time.sleep(2)

    n=randint(1,6)
    print(f"{player3}: {n}")
    k=k+n
    time.sleep(2)

    n=randint(1,6)
    print(f"{player4}: {n}")
    h=h+n
    time.sleep(2)

    if r>10 and r>m and r>k and r>h:
        print(f"Congratulation!! {player1} you have won suiiiii!!!")
        break

    elif m>10 and m>r and m>k and m>h:
        print(f"Congratulation!! {player2} you have won Ankara Messi!!!")
        break

    elif k>10 and k>r and k>m and k>h:
        print(f"Congratulation!! {player3} you have won Dictator!!!")
        break

    elif h>10 and h>r and h>k and h>m:
        print(f"Congratulation!! {player4} you have won Viking!!!")
        break

    else:
        pass
    print("__"*30)
    print()
print("__"*30)
print()